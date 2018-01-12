import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import json
import os
from src.fetchFunction.video_service.fields.audio import Audio

class AudioTest(unittest.TestCase):
    
    
    def setUp(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        self.baseData = json.load(open(path))

        self.mockedTextRespo = type('lamdbaobject', (object,), {})()

    @patch('src.fetchFunction.video_service.fields.audio.requests')
    def test_fetch_failed(self, requestsMock):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'AudioApi', 'mocks', 'audio.m3u')
        adM3uData = open(path).read()

        self.mockedTextRespo.text = adM3uData
        requestsMock.get = MagicMock(return_value=self.mockedTextRespo)
        
        audio = Audio()
        res = audio.fetch(self.baseData)
         
        assert requestsMock.get.called
        self.assertEqual('English - All Audio', res[0]['title'])
        self.assertEqual('English Music Off', res[1]['title'])
        self.assertEqual('English Pumped Up Music', res[2]['title'])
        self.assertEqual('Spanish', res[3]['title'])
        
        self.assertEqual(4, len(res))