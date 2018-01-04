class Captions:

    def fetch(self, raysData):
        returnArr = []

        for key, val in enumerate(raysData['media$content']):
            if val['plfile$format'] != "SRT":
                continue
            tempRow = {
                'type': val['plfile$format'],
                'language': val['plfile$language'],
                'filesize': val['plfile$fileSize'],
                'url': val['plfile$url'],
            }

            returnArr.append(tempRow)

        return returnArr