import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')

# Helper function to convert Decimal to int/float
def decimal_to_native(obj):
    if isinstance(obj, list):
        return [decimal_to_native(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: decimal_to_native(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        # convert Decimal to int or float
        return int(obj) if obj % 1 == 0 else float(obj)
    else:
        return obj

def lambda_handler(event, context):
    try:
        if not event.get("pathParameters") or not event["pathParameters"].get("id"):
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Product ID is required"})
            }

        product_id = event["pathParameters"]["id"]

        response = table.get_item(
            Key={"productId": product_id}
        )

        if "Item" not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Product not found"})
            }

        item = decimal_to_native(response["Item"])

        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }
