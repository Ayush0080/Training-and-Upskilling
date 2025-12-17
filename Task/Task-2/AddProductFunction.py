import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    item = {
        "productId": str(uuid.uuid4()),
        "name": body["name"],
        "price": body["price"]
    }

    table.put_item(Item=item)

    return {
        "statusCode": 201,
        "body": json.dumps(item)
    }
