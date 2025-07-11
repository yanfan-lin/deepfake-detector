import os
import json
import boto3
from botocore.exceptions import ClientError


# Constants for the S3 bucket and region.
BUCKET_NAME = 'yfldeepfake'
REGION_NAME = 'us-west-1'

def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name=REGION_NAME)
    
    # Extract the filename from query parameters.
    query_params = event.get('queryStringParameters') or {}
    file_name = query_params.get('filename')
    
    if not file_name:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Missing filename parameter'})
        }
    
    try:
        # Sanitize the filename: remove spaces and extract the base name.
        file_name = str(file_name).replace(" ", "_")
        file_name = file_name.split("/")[-1]

        # Generate the presigned POST URL
        presigned_post = s3.generate_presigned_post(
            Bucket=BUCKET_NAME,
            Key=file_name,
            ExpiresIn=3600 #exxpiration time in seconds 
        )
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(presigned_post)
        }
    except ClientError as ce:
        return {
            'statusCode': 502,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Failed to generate presigned URL.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
