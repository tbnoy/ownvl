from .platform_feed import PlatformFeed
from .ProfileApi import ProfileApi
import requests
from fetchFunction.config.conf import conf

def getPlatform():
    url = conf['platformUrl']
    
    return PlatformFeed(url, requests)    

def getProfileApi():
    waiversUrl = conf['waiversUrl']
    authUrl = conf['authUrl']
    token = conf['profileToken']

    return ProfileApi(authUrl, waiversUrl, token)