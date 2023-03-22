import json
import boto3
from botocore.exceptions import ClientError


tableName = "my-table"
dynamo = boto3.client('dynamodb')

def returnFun(status,body):
    return{
        "statusCode":status,
        "body":json.dumps(body)
            
    }
def specData(book_id):
    response = dynamo.get_item(
        TableName=tableName,
        Key={
            'id': {'S': book_id}
            
        })
    return(response)

def getData():
    response = dynamo.scan(TableName=tableName)
    return(response['Items'])

def putData(item):
    try:
        response = dynamo.put_item(TableName=tableName,Item=item)
        return(response['ResponseMetadata']['HTTPStatusCode'])
    except ClientError as e:
        return(400)
def deleteData(book_id):
    response = dynamo.delete_item(TableName=tableName,Key={'id': {'S': book_id}})
    return(response)
    
def updateData(book_id,ExpressionAttributeNames,ExpressionAttributeValues,UpdateExpression):
    response = dynamo.update_item(
        ExpressionAttributeNames=ExpressionAttributeNames,
        ExpressionAttributeValues=ExpressionAttributeValues,Key={'id': {'S': book_id}},
        UpdateExpression=UpdateExpression,
        TableName=tableName)
    return(response)


def lambda_handler(event, context):
    if(event['httpMethod']=='GET'):
        if event['pathParameters']!=None:
            book_id = event['pathParameters']['id']
            response = specData(book_id)
            if 'Item' in response:
                return(returnFun(200,response['Item']))
            else:
                return(returnFun(404,'Book not found'))
        else:
            data=getData()
            return(returnFun(200,data))
    elif(event['httpMethod']=='POST'):
        item=json.loads(event['body'])
        statusCode = putData(item)
        if(statusCode == 200):
            return(returnFun(200,"Succesfully Item updated"))
        else:
            return(returnFun(400,"Please send item with correct schema"))
    elif(event['httpMethod']=='DELETE'):
        if event['pathParameters']!=None:
            book_id = event['pathParameters']['id']
            response = deleteData(book_id)
            return(returnFun(200,response))
    elif(event['httpMethod']=='PUT'):
        print(event)
        if event['pathParameters']!=None:
            book_id = event['pathParameters']['id']
            body=json.loads(event['body'])
            ExpressionAttributeNames=body['ExpressionAttributeNames']
            ExpressionAttributeValues=body['ExpressionAttributeValues']
            UpdateExpression=body['UpdateExpression']
            response=updateData(book_id,ExpressionAttributeNames,ExpressionAttributeValues,UpdateExpression)
            return(returnFun(200,response))
    else:
        data="Unknown method"
        statusCode=200
        print(event)
        return{
            "statusCode":statusCode,
            "body":json.dumps(data)
        }

