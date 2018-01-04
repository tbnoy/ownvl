import unittest
from unittest.mock import MagicMock
from fetchFunction.feed_data.platform_feed import PlatformFeed

class PlatformFeedTest(unittest.TestCase):

    def test_fetch_base_found(self):
        url = 'url'
        guid = 'guid'
        someResult = 'someResult'

        requestsRespo = MagicMock()
        waiversApiReturn = {
            "entries": [someResult]
        }
        requestsRespo.json = MagicMock(return_value=waiversApiReturn)


        requests = MagicMock()
        requests.get = MagicMock(return_value=requestsRespo)

        platformFeed = PlatformFeed(url, requests)
        
        self.assertEqual(
            someResult,
            platformFeed.fetchBase(guid)
        )

    def test_fetch_base_not_found(self):
        url = 'url'
        guid = 'guid'
        someResult = 'someResult'

        requestsRespo = MagicMock()
        waiversApiReturn = {
            "entries": []
        }
        requestsRespo.json = MagicMock(return_value=waiversApiReturn)

        requests = MagicMock()
        requests.get = MagicMock(return_value=requestsRespo)

        platformFeed = PlatformFeed(url, requests)

        try:
            platformFeed.fetchBase(guid)
        except Exception as ex:
            self.assertEqual('Video with guid: guid, not found on base', str(ex))
        








    def test_fetch_rays_found(self):
        url = 'url'
        guid = 'guid'
        someResult = 'someResult'

        requestsRespo = MagicMock()
        waiversApiReturn = {
            "entries": [someResult]
        }
        requestsRespo.json = MagicMock(return_value=waiversApiReturn)


        requests = MagicMock()
        requests.get = MagicMock(return_value=requestsRespo)

        platformFeed = PlatformFeed(url, requests)
        
        self.assertEqual(
            someResult,
            platformFeed.fetchRays(guid)
        )

    def test_fetch_rays_not_found(self):
        url = 'url'
        guid = 'guid'
        someResult = 'someResult'

        requestsRespo = MagicMock()
        waiversApiReturn = {
            "entries": []
        }
        requestsRespo.json = MagicMock(return_value=waiversApiReturn)

        requests = MagicMock()
        requests.get = MagicMock(return_value=requestsRespo)

        platformFeed = PlatformFeed(url, requests)

        try:
            platformFeed.fetchRays(guid)
        except Exception as ex:
            self.assertEqual('Video with guid: guid, not found on rays', str(ex))
        