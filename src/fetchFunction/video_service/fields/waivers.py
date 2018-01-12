from src.fetchFunction.feed_data.factories import getProfileApi

class Waivers:

    def __init__(self, profileApi):
        self.profileApi = profileApi

    def fetch(self, baseData, raysData, params, language):
        returnArr = {}
        profileApi = getProfileApi()
        
        linkId = baseData['media$content'][0]['plfile$releases'][0]['plrelease$pid']
        
        data = {
            'videoId': params['videoGuid'],
            'profileId': params['profileGuid'],
            'linkId': linkId,
            'platform': params['platform'],
            'language': language
        }

        res = self.profileApi.getWaivers(data)
    
        if 'errorCode' in res:
            returnArr['code'] = res['errorCode']
            returnArr['status'] = "error"
            returnArr['errorMessage'] = res.get('userMessage', '')
        else:
            returnArr = res['items'][0];
        
        return returnArr