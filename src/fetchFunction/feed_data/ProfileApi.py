import requests

class ProfileApi:

    def __init__(self, authUrl, waiversUrl, profileToken):
        self.authUrl = authUrl
        self.waiversUrl = waiversUrl
        self.slug = None

        self.headers = {
            'Authorization': profileToken,
            'Accept': 'application/json',
        }

    def getVideoAuth(self, data):
        payload = {
            'videoId': data['videoId'],
            'profileId': data['profileId'],
            'linkId': data['linkId'],
            'platform': data['platform'],
            'language': data['language']
        }
        
        try:
            r = requests.get(self.authUrl+'/video/authorize', params=payload, headers=self.headers)
            json = r.json()
        except requests.exceptions.RequestException as e:
            raise Exception("We had an with Auth")

        self.slug = json.get('waiverSlug', None)

        return json

    def getWaivers(self, data):
        if self.slug == None:
            self.getVideoAuth(data)

        payload = {
            'platform': data['platform'],
            'slug': self.slug
        }
        try:
            r = requests.get(self.waiversUrl+'/waivers', params=payload, headers=self.headers)
            json = r.json()
        except requests.exceptions.RequestException as e:
            raise Exception("We had an with waivers")

        return json
