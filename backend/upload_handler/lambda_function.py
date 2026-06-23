import os
import boto3
from botocore.config import Config


def lambda_handler(event, context):
    s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
    bucket_name = os.getenv('S3_BUCKET_NAME')
    file_name = event.get('fileName', 'unknown')
    ttl = int(os.getenv('PRESIGNED_URL_TTL', 900))

    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket_name, 'Key': file_name},
        ExpiresIn=ttl
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': json.dumps({
            'uploadUrl': presigned_url,
            'fileKey': file_name
        })
    }


import json
