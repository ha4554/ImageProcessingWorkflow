from PIL import Image
import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['source_bucket']
    target_bucket = event['target_bucket']
    key = event['key']

    download_path = f"/tmp/{key}"
    upload_path = f"/tmp/thumbnail-{key}"

    # Download original image
    s3.download_file(source_bucket, key, download_path)

    # Resize image
    with Image.open(download_path) as img:
        img.thumbnail((200, 200))
        img.save(upload_path)

    # Upload thumbnail
    s3.upload_file(upload_path, target_bucket, f"thumbnail-{key}")

    return {"status": "success", "thumbnail": f"thumbnail-{key}"}