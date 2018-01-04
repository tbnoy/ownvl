import unittest
from unittest.mock import MagicMock
import json
import os
from fetchFunction.video_service.fields.auth import Auth

class AuthTest(unittest.TestCase):
    
    def test_fetch_failed(self):
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

        platform = 'web'
       
        profileApi = MagicMock()
        profileApiReturn = {
            "errorCode": "err_code",
            "userMessage": "asd"
        }
        profileApi.getVideoAuth = MagicMock(return_value=profileApiReturn)
        
        auth = Auth(profileApi)
        res = auth.fetch(baseData, raysData, params, language)
         
        self.assertEqual(profileApiReturn['errorCode'], res['code'])
        self.assertEqual('error', res['status'])
        self.assertEqual(profileApiReturn['userMessage'], res['errorMessage'])

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

        platform = 'web'
       
        profileApi = MagicMock()
        profileApiReturn = {
            "videoAuthSignature": "",
            "requirewaiver": False,
            "waiverSlug": "tbird-waiver"
        }
           
        profileApi.getVideoAuth = MagicMock(return_value=profileApiReturn)
        
        auth = Auth(profileApi)
        res = auth.fetch(baseData, raysData, params, language)
         
        self.assertEqual(profileApiReturn['videoAuthSignature'], res['signature'])
        self.assertEqual(profileApiReturn['requirewaiver'], res['requireWaiver'])
        self.assertEqual(profileApiReturn['waiverSlug'], res['waiverSlug'])