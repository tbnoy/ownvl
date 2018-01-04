import unittest
import json
import os
from fetchFunction.video_service.fields.rays import Rays

class RaysTest(unittest.TestCase):
    
    def test_fetch_with_success(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'rays.json')
        raysData = json.load(open(path))

        rays = Rays()
        res = rays.fetch(raysData)
         
        self.assertEqual("abcdefg", "".join(res))

    def test_fetch_with_missing_rays(self):
        
        raysData = {
            "media$content": []
        }

        rays = Rays()
        res = rays.fetch(raysData)
         
        self.assertEqual("", "".join(res))