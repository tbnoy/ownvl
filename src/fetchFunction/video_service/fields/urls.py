import xml.etree.ElementTree as ET

class Urls:

    def fetch(self, baseData, raysData, userGUID, platform):
        return_array = {}

        # temp hack for after refactor
        feedIDStd = 'B0Xsr4HI9Tzx'
        feedIDRays = 'playback_rays'
        queryString = self.retrievePlatformQueryString(userGUID, platform)

        # URLs
        return_array["playbackStandard"] = "%s%s" % (baseData['media$content'][0]['plfile$url'], queryString)
        return_array["playbackSecure"] = "%s%s%s" % (baseData['media$content'][1]['plfile$url'], queryString, "&sig=")

        # For the Rays URL, find the first media object listed in the Rays Feed.
        for key, value in enumerate(raysData['media$content']):
            # If it's a video, grab it now.
            if value['plfile$format'] == "M3U":
                return_array["playbackRays"] = "%s%s%s" % (value['plfile$url'], queryString, "&rays=")
                break
        
        return_array["feedStandard"] = self.retrieveFeedURL(feedIDStd, baseData['guid'])
        return_array["feedRays"] = self.retrieveFeedURL(feedIDRays, baseData['guid'])
        return_array["smil"] = baseData['media$content'][0]['plfile$url']

        return return_array

    def retrievePlatformQueryString(self, userGUID, platform):
        return "%s%s%s%s" % ("&bbuid=", userGUID, "&formats=m3u&embedded=true&tracking=true&platform=", platform)

    def retrieveFeedURL(self, feedID, videoGUID):
        return "%s%s%s%s" % ("https://feed.theplatform.com/f/VSsHaC/", feedID, "?form=json&byGuid=", videoGUID)