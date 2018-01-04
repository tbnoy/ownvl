import requests

class Audio:

    def fetch(self, baseData):
        returnArr = []

        manifestURL = baseData['media$content'][0]['plfile$url']
        response = requests.get(manifestURL)
        
        manifestContents = response.text

        lines = manifestContents.split("#")

        for value in lines:
            if value.find("EXT-X-MEDIA:TYPE=AUDIO") > -1:
                audioTracks = value.split(',')

                tempDict = {}

                tempDict["title"] = self.retrieveValueWithSearchKey("NAME", audioTracks)
                tempDict["language"] = self.retrieveValueWithSearchKey("LANG", audioTracks)
                tempDict["default"] = (self.retrieveValueWithSearchKey("DEFAULT", audioTracks) == "YES")
                tempDict["format"] = self.retrieveValueWithSearchKey("GROUP", audioTracks)
                tempDict["url"] = self.retrieveValueWithSearchKey("URI", audioTracks)

                returnArr.append(tempDict)
        return returnArr

    def retrieveValueWithSearchKey(self, searchKey, searchArray):
        returnVal = ""

        for idx, val in enumerate(searchArray):
            if val.find(searchKey) > -1:
                startIndex = val.find("=") + 1
                desiredVal = val[startIndex:]

                if desiredVal[0] == '"':
                    desiredVal = desiredVal[1:len(desiredVal)-1]

                returnVal = desiredVal
                break

        return returnVal;