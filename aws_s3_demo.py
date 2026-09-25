import boto3
from botocore.exceptions import ClientError

REGION = "us-west-2"
s3 = boto3.client("s3", region_name=REGION)

file_name = "sample.txt"
with open(file_name, "w") as f:
    f.write("Hello from AWS Boto3!")

bucket_name = "my-sharon-lab-bucket-2026"

print(f"Uploading {file_name} to {bucket_name}...")
try:
    s3.upload_file(file_name, bucket_name, file_name)
    print("Upload complete!")
except ClientError as e:
    print(f"Upload failed: {e}")