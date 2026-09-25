import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

print("Listing S3 Buckets:")
response = s3.list_buckets()
buckets = response.get('Buckets', [])

if buckets:
    for bucket in buckets:
        print(f"- {bucket['Name']}")
else:
    print("No existing buckets found in this account.")

# Practice creating a file
file_name = "sample.txt"
with open(file_name, "w") as f:
    f.write("Hello from AWS Boto3!")

print(f"Created local sample file: {file_name}")