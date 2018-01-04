import json
import os
from fetchFunction.video_service.video_service import VideoService
from fetchFunction.feed_data.factories import getProfileApi
from fetchFunction.config.conf import conf
# from .fields.urls import Urls

# serverless invoke local -f fetch -d '{"vid": "CDF001B001B", "profile": "5F5DA2E8-D4EF-45FA-AB7B-F49A6A3226DE", "platform": "web"}'

def fetch(event, context):
    
    params = {
        "videoGuid": event['queryStringParameters'].get("guid"),
        "profileGuid": event['queryStringParameters'].get("profile"),
        "platform": event['queryStringParameters'].get("platform"),
        "fields": event['queryStringParameters'].get("fields")
    }

    # body["event"] = event['queryStringParameters']
    # body["event"] = event['queryStringParameters'].get('guid')
    
    vs = VideoService()
    res = vs.fetch(params)

    response = {
        "statusCode": 200,
        "isBase64Encoded": False,
        "headers": {"x-test-header" : "foobar"},
        "body": json.dumps(res),
    }
    return response