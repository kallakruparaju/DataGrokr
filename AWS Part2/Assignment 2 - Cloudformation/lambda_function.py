import json
import boto3
import cfnresponse

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print(event)
    vpc_id = event['ResourceProperties']['VpcId']
    try:
        response = ec2.describe_vpcs(VpcIds=[vpc_id])
        cidr_ip = response['Vpcs'][0]['CidrBlock']
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {'CidrIp': cidr_ip})
    except Exception as e:
        print(e)
        cfnresponse.send(event, context, cfnresponse.FAILED, {})
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
