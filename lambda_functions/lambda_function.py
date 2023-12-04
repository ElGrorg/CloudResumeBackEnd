import json
import boto3

def lambda_handler(event, context):
    
    # Connect to DynamoDB resource
    client = boto3.resource('dynamodb')
    
    # Create a DynamoDB Client to the visitor_count table
    table = client.Table('visitor_count')
    
    # Increment visitor_count for index.html key
    response = table.update_item(
        Key={
            'path': 'index.html'
        },
        AttributeUpdates={
            'visitor_count': {
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    # Get visitor_count from response
    response = table.get_item(
        Key={
            'path': 'index.html'
        }
    )

    visitor_count = response['Item']['visitor_count']
    # Return visitor_count to user
    return {
        'statusCode': 200,
        'body': visitor_count
    }
