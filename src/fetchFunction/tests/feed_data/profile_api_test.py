import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from fetchFunction.feed_data.ProfileApi import ProfileApi

class ProfileApiTest(unittest.TestCase):

    @patch('fetchFunction.feed_data.ProfileApi.requests')
    def test_getVideoAuth(self, requestsMock):
        authUrl = 'authUrl'
        waiversUrl = 'waiversUrl'
        profileToken = 'profileToken'
        waiverSlug = 'waiverSlug'
        data = {
            'videoId': 1,
            'profileId': 1,
            'linkId': 1,
            'platform': 1,
            'language': 1,
        }

        someResult = 'someResult'

        requestsRespo = MagicMock()
        waiversApiReturn = {
            "waiverSlug": waiverSlug
        }
        requestsRespo.json = MagicMock(return_value=waiversApiReturn)

        requests = MagicMock()
        requestsMock.get = MagicMock(return_value=requestsRespo)

        profileApi = ProfileApi(authUrl, waiversUrl, profileToken)
        
        self.assertEqual(
            waiversApiReturn,
            profileApi.getVideoAuth(data)
        )

    @patch('fetchFunction.feed_data.ProfileApi.requests')
    def test_getWaivers_mockSlug(self, requestsMock):
        authUrl = 'authUrl'
        waiversUrl = 'waiversUrl'
        profileToken = 'profileToken'
        waiverSlug = 'waiverSlug'
        data = {
            'videoId': 1,
            'profileId': 1,
            'linkId': 1,
            'platform': 1,
            'language': 1,
        }

        someResult = 'someResult'

        requestsRespo = MagicMock()
        waiversApiReturn = {
            "waiverSlug": waiverSlug
        }
        requestsRespo.json = MagicMock(return_value=waiversApiReturn)

        requests = MagicMock()
        requestsMock.get = MagicMock(return_value=requestsRespo)

        profileApi = ProfileApi(authUrl, waiversUrl, profileToken)
        profileApi.slug = 'something'
        
        self.assertEqual(
            waiversApiReturn,
            profileApi.getWaivers(data)
        )

    @patch('fetchFunction.feed_data.ProfileApi.requests')
    def test_getWaivers_needToCallAuth(self, requestsMock):
        authUrl = 'authUrl'
        waiversUrl = 'waiversUrl'
        profileToken = 'profileToken'
        waiverSlug = 'waiverSlug'
        data = {
            'videoId': 1,
            'profileId': 1,
            'linkId': 1,
            'platform': 1,
            'language': 1,
        }

        someResult = 'someResult'

        requestsRespo = MagicMock()
        waiversApiReturn = {
            "waiverSlug": waiverSlug
        }
        requestsRespo.json = MagicMock(return_value=waiversApiReturn)

        requestsMock.get = MagicMock()
        requestsMock.get.side_effect = [requestsRespo, requestsRespo]


        profileApi = ProfileApi(authUrl, waiversUrl, profileToken)
        
    
        self.assertEqual(
            waiversApiReturn,
            profileApi.getWaivers(data)
        )
        self.assertEqual(requestsMock.get.call_count, 2)