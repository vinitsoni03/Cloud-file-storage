#!/bin/bash

echo "Deploying cloud-file-storage..."

# Package Lambda functions
cd backend/upload_handler && zip -r ../../upload_handler.zip . && cd ../..
cd backend/retrieve_handler && zip -r ../../retrieve_handler.zip . && cd ../..
cd backend/delete_handler && zip -r ../../delete_handler.zip . && cd ../..

echo "Deployment complete"
