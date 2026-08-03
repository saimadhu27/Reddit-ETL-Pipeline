from utils.constants import AWS_REGION, AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY
import boto3
from botocore.exceptions import ClientError

def connect_to_s3():
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_ACCESS_KEY,
            region_name=AWS_REGION
        )
        return s3
    except Exception as e:
        print(f"Error connecting to S3: {e}")
        raise
        
def create_bucket_if_not_exists(s3, bucket_name):
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': AWS_REGION})
            print(f"Bucket '{bucket_name}' created.")
        else:
            print(f"Error checking/creating bucket: {e}")
            raise
            
def upload_to_s3(s3, file_path, bucket_name, object_name):
    try:
        key = f"raw/{object_name}"
        s3.upload_file(file_path, bucket_name, key)
        print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{key}'.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        raise