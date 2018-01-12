import unittest
import json
import os
from src.fetchFunction.video_service.fields.captions import Captions

class CaptionsTest(unittest.TestCase):
    
    def test_fetch(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'rays.json')
        data = json.load(open(path))
        
        captions = Captions()
        res = captions.fetch(data)
        
        self.assertEqual(data['media$content'][1]['plfile$format'], res[0]['type'])
        self.assertEqual(data['media$content'][1]['plfile$language'], res[0]['language'])
        self.assertEqual(data['media$content'][1]['plfile$fileSize'], res[0]['filesize'])
        self.assertEqual(data['media$content'][1]['plfile$url'], res[0]['url'])