class Modifiers:

    def __init__(self, platformFeed):
        self.platformFeed = platformFeed

    def fetch(self, baseData):
        returnArr = []

        basePoint = baseData['pl1$relatedVideos']
        for key, val in enumerate(basePoint):
            try:
                res = self.platformFeed.fetchBase(basePoint[val])
                tempRes = {
                    'guid': val,
                    'title': res['title'],
                    'url': res['media$content'][0]['plfile$url'],
                }
                returnArr.append(tempRes)
            except Exception:
                pass

        return returnArr