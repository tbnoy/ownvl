import unittest
from unittest.mock import MagicMock
import json
import os
from fetchFunction.video_service.fields.modifiers import Modifiers

class ModifiersTest(unittest.TestCase):
    
    def test_fetch_with_error(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        baseData = json.load(open(path))

       
        platformFeed = MagicMock()
        platformFeedReturn = {
            "title": "someTitle",
            "media$content": [
                {'plfile$url': 'urlHere'}
            ]
        }
        platformFeed.fetchBase = MagicMock(return_value=platformFeedReturn)
       

        modifiers = Modifiers(platformFeed)
        res = modifiers.fetch(baseData)
         
        self.assertEqual('mod.1', res[0]['guid'])
        self.assertEqual('someTitle', res[0]['title'])
        self.assertEqual('urlHere', res[0]['url'])