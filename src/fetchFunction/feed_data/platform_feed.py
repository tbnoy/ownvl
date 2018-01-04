import requests

class PlatformFeed:

    def __init__(self, url, requests):
        self.url = url
        self.requests = requests

    def fetchBase(self, guid): 
        payload = {'form': 'json', 'byGuid': guid}
                
        try:
            r = self.requests.get(self.url+'/f/VSsHaC/B0Xsr4HI9Tzx', params=payload)
            json = r.json()
        except requests.exceptions.RequestException as e:
            raise Exception("We had an error with base for: "+guid)

        entries = json.get('entries', [])
        if len(entries) == 0:
            raise Exception("Video with guid: "+guid+", not found on base")

        return entries[0]

    def fetchRays(self, guid): 
        payload = {'form': 'json', 'byGuid': guid}

        try:
            r = self.requests.get(self.url+'/f/VSsHaC/playback_rays', params=payload)
            json = r.json()
        except requests.exceptions.RequestException as e:
            raise Exception("We had an error with rays for: "+guid)
        
        entries = json.get('entries', [])

        if len(entries) == 0:
            raise Exception("Video with guid: "+guid+", not found on rays")

        return entries[0]