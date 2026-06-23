provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "file_storage" {
  bucket = "vinit-file-storage-prod"

  tags = {
    Name = "Cloud File Storage Bucket"
  }
}

resource "aws_s3_bucket_public_access_block" "file_storage" {
  bucket = aws_s3_bucket.file_storage.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
