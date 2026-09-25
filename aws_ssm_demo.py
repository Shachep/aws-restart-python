import boto3
from botocore.exceptions import ClientError

ssm = boto3.client('ssm')

# 1. Put a parameter into SSM Parameter Store
param_name = "/my-app/dev/db_url"
param_value = "postgres://admin:secret123@db.example.com:5432/mydb"

print(f"Storing parameter: {param_name}")

try:
    ssm.put_parameter(
        Name=param_name,
        Value=param_value,
        Type='String',
        Overwrite=True
    )
    print("Parameter successfully created!")

    # 2. Retrieve the parameter back
    print(f"\nFetching parameter: {param_name}")
    response = ssm.get_parameter(Name=param_name)
    
    retrieved_value = response['Parameter']['Value']
    print(f"Retrieved Value: {retrieved_value}")

except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'AccessDeniedException':
        print("\nAccess Denied: Your IAM role does not have permission for SSM Parameter Store operations.")
    else:
        print(f"\nAn error occurred: {e}")