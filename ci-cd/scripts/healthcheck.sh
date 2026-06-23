#!/bin/bash

echo "Running health check..."

API_URL="${API_GATEWAY_URL}"
if [ -z "$API_URL" ]; then
    echo "API URL not set"
    exit 1
fi

response=$(curl -s -o /dev/null -w "%{http_code}" "$API_URL/files")

if [ "$response" = "200" ]; then
    echo "Health check passed!"
    exit 0
else
    echo "Health check failed: $response"
    exit 1
fi
