import json
import boto3
import base64


dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    for records in event['Records']:
        partitionKey=records['kinesis']['partitionKey']
        sequenceNumber=records['kinesis']['sequenceNumber']
        data=records['kinesis']['data']
        data = base64.b64decode(data).decode('utf-8')
    response = dynamodb.put_item( 
        TableName='my-table-name',
        Item={ 
            "sequenceNumber": {
                "S": sequenceNumber
            },
            "partitionKey": {
                "S": partitionKey
            },
            "data": {
                "S": data
            }
        })
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }