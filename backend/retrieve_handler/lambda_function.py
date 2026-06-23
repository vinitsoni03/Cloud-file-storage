import os
import boto3
from botocore.config import Config


def lambda_handler(event, context):
    s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
    bucket_name = os.getenv('S3_BUCKET_NAME')
    ttl = int(os.getenv('PRESIGNED_URL_TTL', 900))

    response = s3.list_objects_v2(Bucket=bucket_name)
    files = []

    if 'Contents' in response:
        for obj in response['Contents']:
            presigned_url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': obj['Key']},
                ExpiresIn=ttl
            )
            files.append({
                'key': obj['Key'],
                'url': presigned_url,
                'size': obj['Size'],
                'lastModified': obj['LastModified'].isoformat()
            })

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        'body': json.dumps({'files': files})
    }


import json
