# ImageProcessingWorkflow

## Architecture
- Lambda Function: resize images
- Step Functions: orchestrates workflow
- S3 Buckets: original-images-huy2025, resized-images-huy2025
- API Gateway: triggers Step Function

## Prerequisites
- AWS account
- Python 3.11 runtime
- Pillow layer

## Deployment Instructions
1. Create S3 buckets:
   - original-images-huy2025
   - resized-images-huy2025
2. Deploy Lambda function:
   - Upload `lambda_function.py` and attach Pillow Layer
3. Create Step Functions state machine:
   - Use `step_function.json`
   - Region: Canada Central (ca-central-1)
4. Create API Gateway:
   - Method: POST
   - Integration: Lambda non-proxy
   - Endpoint: https://wkg49sf8v8.execute-api.ca-central-1.amazonaws.com/prod/process-image
5. Test:
   - Upload an image to `original-images-huy2025`
   - Check resized image in `resized-images-huy2025`