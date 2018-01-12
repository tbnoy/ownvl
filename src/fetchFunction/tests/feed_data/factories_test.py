import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from src.fetchFunction.feed_data.factories import getPlatform
from src.fetchFunction.feed_data.factories import getProfileApi

class FactoriesTest(unittest.TestCase):

    @patch('src.fetchFunction.config.conf')
    def test_getPlatform(self, confMock):
        someUrl = 'someUrl'

        confMock = {
            'platformUrl': someUrl
        }
        
        res = getPlatform()
        
        name = type(res).__name__
        
        self.assertEqual('PlatformFeed', name)

    @patch('src.fetchFunction.config.conf')
    def test_getProfileApi(self, confMock):
        confMock = {
            'waiversUrl': 'waiversUrl',
            'authUrl': 'authUrl',
            'token': 'profileToken',
        }
        
        res = getProfileApi()
        
        name = type(res).__name__
        
        self.assertEqual('ProfileApi', name)