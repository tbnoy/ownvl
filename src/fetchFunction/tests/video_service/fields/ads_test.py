import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import json
import os
from src.fetchFunction.video_service.fields.ads import Ads

class AudioTest(unittest.TestCase):
    
    def setUp(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        self.baseData = json.load(open(path))

        self.mockedTextRespo = type('lamdbaobject', (object,), {})()

    @patch('src.fetchFunction.video_service.fields.ads.requests')
    def test_fetch_failed(self, requestsMock):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'AdApi', 'mocks', 'ad.m3u')
        adM3uData = open(path).read()

        self.mockedTextRespo.text = adM3uData
        requestsMock.get = MagicMock(return_value=self.mockedTextRespo)

        userGUID = 'xxxx'
        platform = 'web'
        
        ads = Ads()
        res = ads.fetch(self.baseData, userGUID, platform)
        
        assert requestsMock.get.called
        self.assertEqual('postroll', res[0]['type'])
        self.assertEqual('false', res[0]['noSkip'])
        
        self.assertEqual(1, len(res))