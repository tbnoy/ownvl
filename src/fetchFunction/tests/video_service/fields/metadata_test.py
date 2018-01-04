import unittest
import json
import os
from fetchFunction.video_service.fields.metadata import Metadata

class MetadataTest(unittest.TestCase):
    
    def test_fetch(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        data = json.load(open(path))
        
        metadata = Metadata()
        res = metadata.fetch(data)
        
        self.assertEqual(data['guid'], res['guid'])
        self.assertEqual(data['title'], res['title'])
        self.assertEqual(data['description'], res['description'])
        self.assertEqual(data['media$content'][0]['plfile$duration'], res['duration'])
        self.assertEqual(data['pl1$videoType'][0], res['type'])
        self.assertEqual(data['media$content'][0]['plfile$releases'][0]['plrelease$pid'], res['pid'])
        self.assertEqual(data['pl1$programTitle'], res['program'])
        self.assertEqual(data['pl1$brandAbbrev'], res['brandCode'])
        self.assertEqual(data['plmedia$chapters'], res['chapters'])
        self.assertEqual(0, res['resumePoint'])