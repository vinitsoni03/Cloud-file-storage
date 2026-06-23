import os
import boto3


def get_s3_client():
    return boto3.client('s3')


def get_bucket_name():
    return os.getenv('S3_BUCKET_NAME')
