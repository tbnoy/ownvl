import json
import os
from fetchFunction.video_service.video_service import VideoService
from fetchFunction.feed_data.factories import getProfileApi
from fetchFunction.config.conf import conf


def respond(data):
    return {
        "code": 200,
        "status": "success",
        "data": data
    }

conf['authUrl'] = "https://profile-dom-origin.api.beachbodyondemand.com"
conf['waiversUrl'] = "https://content-dom-origin.api.beachbodyondemand.com/"
conf['platformUrl'] = "https://feed.theplatform.com"
conf['profileToken'] = "JWpFAHpc6DrkVX3OdFiOwUyhSo6faDpK"

vs = VideoService()
params = {
    "videoGuid": "CDF001B001B",
    "profileGuid": "5F5DA2E8-D4EF-45FA-AB7B-F49A6A3226DE",
    "platform": "web",
    "fields": "waivers"
}
res = vs.fetch(params)

print(json.dumps(respond(res)))