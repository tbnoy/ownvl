class Thumbnail:

    def fetch(self, baseData):
        return {
            'image': baseData['media$thumbnails'][0]['plfile$url'],
            'width': baseData['media$thumbnails'][0]['plfile$width'],
            'height': baseData['media$thumbnails'][0]['plfile$height'],
            'fileSize': baseData['media$thumbnails'][0]['plfile$fileSize'],
        }