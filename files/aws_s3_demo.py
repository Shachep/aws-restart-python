import boto3

s3 = boto3.client('s3')

# 1. List existing buckets
print("Listing S3 Buckets:")
response = s3.list_buckets()

buckets = response.get('Buckets', [])

if buckets:
    for bucket in buckets:
        print(f" - {bucket['Name']}")
        
    # Use the first available bucket to upload a test file
    target_bucket = buckets[0]['Name']
    file_name = "sample.txt"
    
    with open(file_name, "w") as f:
        f.write("Hello from AWS Boto3!")
        
    print(f"\nUploading {file_name} to existing bucket: {target_bucket}...")
    s3.upload_file(file_name, target_bucket, file_name)
    
    # List objects in that bucket
    objects = s3.list_objects_v2(Bucket=target_bucket)
    print("\nFiles in bucket:")
    for obj in objects.get('Contents', []):
        print(f" - {obj['Key']}")
else:
    print("No existing buckets found in this account.")