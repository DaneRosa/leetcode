'''
- Write a Python function to connect to an AWS S3 bucket and download a file.
This question tests your familiarity with AWS services, which is also a required skill for the role.
''' 

import boto3
import botocore

def download_s3_file(bucket_name, s3_file_name, local_file_name):
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(bucket_name).download_file(s3_file_name, local_file_name)
        print("File downloaded successfully.")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

# main
if __name__ == '__main__':
    # download file from S3 bucket
    download_s3_file('my-bucket', 'my_file.txt', 'my_local_file.txt')
    # print file contents
    with open('my_local_file.txt', 'r') as f:
        print(f.read())
        