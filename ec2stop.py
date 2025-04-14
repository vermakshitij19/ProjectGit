import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # change region as needed

# Instance ID to stop
instance_id = 'i-0abc123def456ghij'  # replace with your instance ID

# Stop the instance
response = ec2.stop_instances(InstanceIds=[instance_id])

# Print response
print("Stopping instance:", instance_id)
print(response)

