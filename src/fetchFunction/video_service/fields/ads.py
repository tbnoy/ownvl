import requests
import xml.etree.ElementTree as ET

class Ads:

    def fetch(self, baseData, userGUID, platform):
        returnArray = [];

        params = {
            'bbuid': userGUID,
            'formats': 'm3u',
            'embedded': True,
            'tracking': True,
            'platform': platform,
            'format': 'smil'
        };

        smilFileURL = baseData['media$content'][0]['plfile$url']
        response = requests.get(smilFileURL, params=params)
        smilContents = response.text
        
        tags = smilContents.split("<")
        tags.reverse()
        incrementor = 0

        tree = ET.fromstring(smilContents)
        
        ns = 'http://www.w3.org/2005/SMIL21/Language'
        attributes = tree.findall('./{'+ns+'}body/{'+ns+'}seq/{'+ns+'}ref')[0].attrib

        tempObj = {}

        tempObj["type"] = attributes['tags']
        tempObj["clickout"] = attributes['title']
        tempObj["noSkip"] = attributes['no-skip']
        tempObj["url"] = attributes['src']

        returnArray.append(tempObj)
        
        return returnArray