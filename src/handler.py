import json
import os
from src.fetchFunction.video_service.video_service import VideoService
from src.fetchFunction.feed_data.factories import getProfileApi
from src.fetchFunction.config.conf import conf

# serverless invoke local -f fetch -d '{"queryStringParameters": {"guid": "CDF001B001B", "profile": "5F5DA2E8-D4EF-45FA-AB7B-F49A6A3226DE", "platform": "web", "fields": "metadata"}}'

def fetch(event, context):
    params = {
        "videoGuid": event['queryStringParameters'].get("guid"),
        "profileGuid": event['queryStringParameters'].get("profile"),
        "platform": event['queryStringParameters'].get("platform"),
        "fields": event['queryStringParameters'].get("fields")
    }

    vs = VideoService()
    res = vs.fetch(params)

    response = {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {"x-test-header" : "foobar"},
        "body": json.dumps(res),
    }
    return response