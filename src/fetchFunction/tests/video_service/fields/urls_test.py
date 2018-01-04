import unittest
import json
import os
from fetchFunction.video_service.fields.urls import Urls

class UrlsTest(unittest.TestCase):
    
    def test_fetch(self):
        curDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'newStandart.json')
        baseData = json.load(open(path))
        
        path = os.path.join(curDir, '..', '..', 'FeedData', 'PlatformFeed', 'mocks', 'rays.json')
        raysData = json.load(open(path))

        userGUID = 'xxx-xxx' 
        platform = 'web'

        urls = Urls()
        res = urls.fetch(baseData, raysData, userGUID, platform)

        print(res)
        
        self.assertEqual(
            "%s%s" % (baseData['media$content'][0]['plfile$url'], urls.retrievePlatformQueryString(userGUID, platform)),
            res['playbackStandard']
        )
        self.assertEqual(
            "%s%s%s" % (baseData['media$content'][1]['plfile$url'], urls.retrievePlatformQueryString(userGUID, platform), "&sig="),
            res['playbackSecure']
        )
        self.assertEqual(
            "%s%s%s" % (raysData['media$content'][0]['plfile$url'], urls.retrievePlatformQueryString(userGUID, platform), "&rays="),
            res['playbackRays']
        )
            
        self.assertEqual(
            baseData['media$content'][0]['plfile$url'],
            res['smil']
        )

    def test_retrieveFeedURL(self):
        feedID = 'xxx' 
        videoGUID = 'zzzz'
        urls = Urls()
        res = urls.retrieveFeedURL(feedID, videoGUID)
        
        self.assertEqual(
            "%s%s%s%s" % ("https://feed.theplatform.com/f/VSsHaC/", feedID, "?form=json&byGuid=", videoGUID),
            res
        )