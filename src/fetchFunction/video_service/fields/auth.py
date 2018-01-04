class Auth:

    def __init__(self, profileApi):
        self.profileApi = profileApi

    def fetch(self, baseData, raysData, params, language):
        returnArr = {}
        
        linkId = baseData['media$content'][0]['plfile$releases'][0]['plrelease$pid']

        data = {
            'videoId': params['videoGuid'],
            'profileId': params['profileGuid'],
            'linkId': linkId,
            'platform': params['platform'],
            'language': language
        }

        res = self.profileApi.getVideoAuth(data)
    
        if 'errorCode' in res:
            returnArr['code'] = res['errorCode']
            returnArr['status'] = "error"
            returnArr['errorMessage'] = res.get('userMessage', "")
        else:
            returnArr['signature']       = res.get('videoAuthSignature', "")
            returnArr['requireWaiver']   = res.get('requirewaiver', False)
            returnArr['waiverSlug']      = res.get('waiverSlug', "tbird-waiver")
        
        return returnArr