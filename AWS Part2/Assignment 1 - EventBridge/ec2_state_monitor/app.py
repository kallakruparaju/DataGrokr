import json
import boto3
import os
from botocore.exceptions import ClientError

client = boto3.client('dynamodb')
table_name = os.environ['TABLE_NAME']

def dynamodb_update(instanceid,state,time):
    try:
        response = client.put_item( 
            TableName= table_name,
            Item={
                "instance_id": {
                    "S": instanceid
                },
                "state": {
                    "S": state
                },
                "time": {
                    "S": time
                }
            }
        )
        StatusCode = 200
        Body = "Success"
    except ClientError as e:
        StatusCode = 400
        Body = "Failed"
    return {
        'statusCode': StatusCode,
        'body': json.dumps(Body)
    }

def lambda_handler(event, context):
    instanceid = event['detail']['instance-id']
    state = event['detail']['state']
    time = event['time']
    dynamodb_update(instanceid,state,time)