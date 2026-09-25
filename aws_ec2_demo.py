import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

print("Checking EC2 Instances in this account...")

try:
    response = ec2.describe_instances()
    found_instances = False

    for reservation in response.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            found_instances = True
            instance_id = instance.get('InstanceId')
            state = instance.get('State', {}).get('Name')
            instance_type = instance.get('InstanceType')
            print(f" - ID: {instance_id} | Type: {instance_type} | State: {state}")

    if not found_instances:
        print("No EC2 instances found.")

except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'UnauthorizedOperation':
        print("Access Denied: Your IAM role does not have permission to view EC2 instances.")
    else:
        print(f"An error occurred: {e}")