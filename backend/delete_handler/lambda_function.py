import os
import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = os.getenv('S3_BUCKET_NAME')
    file_key = event.get('fileKey')

    s3.delete_object(Bucket=bucket_name, Key=file_key)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
        },
        'body': json.dumps({'message': 'File deleted successfully'})
    }


import json
