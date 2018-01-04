import unittest
import json
import os
from fetchFunction.video_service.fields.thumbnail import Thumbnail

class ThumbnailTest(unittest.TestCase):
    
    def test_fetch(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        data = json.load(open(path))
        
        thumbnail = Thumbnail()
        res = thumbnail.fetch(data)
        
        self.assertEqual(data['media$thumbnails'][0]['plfile$url'], res['image'])
        self.assertEqual(data['media$thumbnails'][0]['plfile$width'], res['width'])
        self.assertEqual(data['media$thumbnails'][0]['plfile$height'], res['height'])
        self.assertEqual(data['media$thumbnails'][0]['plfile$fileSize'], res['fileSize'])