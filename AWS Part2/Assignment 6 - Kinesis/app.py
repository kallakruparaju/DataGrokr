import json
import boto3
import time

kinesis_client = boto3.client('kinesis')
stream_name = "my-kinesis-stream"
PartitionKey = "111111"

def randomData():
    data_record = {
        'timestamp': int(time.time())
    }
    return data_record

def lambda_handler(event, context):
    data_record = randomData()
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(data_record, indent=2).encode('utf-8'),
        PartitionKey=PartitionKey
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }