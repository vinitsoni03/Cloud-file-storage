import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import boto3
from botocore.exceptions import ClientError
from mangum import Mangum

app = FastAPI(title="Cloud File Storage API", version="1.0.0")
handler = Mangum(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

s3_client = boto3.client("s3")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "cloud-file-storage")
PRESIGNED_URL_TTL = int(os.getenv("PRESIGNED_URL_TTL", "900"))


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/api/files/upload-url")
async def get_upload_url(filename: str):
    try:
        presigned_url = s3_client.generate_presigned_url(
            "put_object",
            Params={"Bucket": S3_BUCKET_NAME, "Key": filename},
            ExpiresIn=PRESIGNED_URL_TTL,
        )
        return {"uploadUrl": presigned_url, "fileKey": filename}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/files")
async def list_files():
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
        files = []
        if "Contents" in response:
            for obj in response["Contents"]:
                download_url = s3_client.generate_presigned_url(
                    "get_object",
                    Params={"Bucket": S3_BUCKET_NAME, "Key": obj["Key"]},
                    ExpiresIn=PRESIGNED_URL_TTL,
                )
                files.append({
                    "key": obj["Key"],
                    "url": download_url,
                    "size": obj["Size"],
                    "lastModified": obj["LastModified"].isoformat(),
                })
        return {"files": files}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/files/{file_key:path}")
async def delete_file(file_key: str):
    try:
        s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=file_key)
        return {"message": "File deleted successfully"}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
