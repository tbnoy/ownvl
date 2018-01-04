class Metadata:

    def fetch(self, baseData):
        return {
            "guid": baseData['guid'],
            "title": baseData['title'],
            "description": baseData['description'],
            "duration": baseData['media$content'][0]['plfile$duration'],
            "type": baseData['pl1$videoType'][0],
            "pid": baseData['media$content'][0]['plfile$releases'][0]['plrelease$pid'],
            "program": baseData['pl1$programTitle'],
            "brandCode": baseData['pl1$brandAbbrev'],
            "chapters": baseData['plmedia$chapters'],
            "resumePoint": 0,
        }