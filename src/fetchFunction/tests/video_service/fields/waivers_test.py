import unittest
from unittest.mock import MagicMock
import json
import os
from fetchFunction.video_service.fields.waivers import Waivers

class WaiversTest(unittest.TestCase):
    
    def test_fetch_with_error(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        baseData = json.load(open(path))

        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'rays.json')
        raysData = json.load(open(path))
        language = 'english'
        params = {
            'videoGuid': 1,
            'profileGuid': 1,
            'platform': 1
        }

        profileApi = MagicMock()
        waiversApiReturn = {
            "errorCode": "xx",
            "userMessage": "some user msg"
        }
        profileApi.getWaivers = MagicMock(return_value=waiversApiReturn)
        platform = 'web'

        waivers = Waivers(profileApi)
        res = waivers.fetch(baseData, raysData, params, language)

        self.assertEqual(waiversApiReturn['errorCode'], res['code'])
        self.assertEqual("error", res['status'])
        self.assertEqual(waiversApiReturn['userMessage'], res['errorMessage'])

    def test_fetch_success(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        baseData = json.load(open(path))

        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'rays.json')
        raysData = json.load(open(path))
        language = 'english'
        params = {
            'videoGuid': 1,
            'profileGuid': 1,
            'platform': 1
        }

        profileApi = MagicMock()
        waiversApiReturn = {
            "items": [
                {"some": "thing"}
            ]
        }
        profileApi.getWaivers = MagicMock(return_value=waiversApiReturn)
        platform = 'web'

        waivers = Waivers(profileApi)
        res = waivers.fetch(baseData, raysData, params, language)
         
        self.assertEqual(waiversApiReturn['items'][0], res)