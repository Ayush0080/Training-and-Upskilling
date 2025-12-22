import json
import urllib3
import boto3
import os

http = urllib3.PoolManager()

SLACK_WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]
AWS_REGION = os.environ["AWS_REGION"]

def send_slack(message):
    payload = {"text": message}
    http.request(
        "POST",
        SLACK_WEBHOOK_URL,
        body=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )

def lambda_handler(event, context):
    detail = event.get("detail", {})
    config_item = detail.get("configurationItem", {})

    resource_type = config_item.get("resourceType", "UNKNOWN")
    resource_id = config_item.get("resourceId", "UNKNOWN")
    region = config_item.get("awsRegion", "UNKNOWN")
    status = config_item.get("configurationItemStatus", "UNKNOWN")

    message_type = detail.get("messageType", "UNKNOWN")

    message = (
        "*AWS CONFIG CHANGE DETECTED*\n"
        f"• Resource Type: `{resource_type}`\n"
        f"• Resource ID: `{resource_id}`\n"
        f"• Region: `{region}`\n"
        f"• Status: `{status}`\n"
        f"• Event Type: `{message_type}`"
    )

    send_slack(message)

    return {
        "status": "OK",
        "resourceType": resource_type,
        "resourceId": resource_id
    }
