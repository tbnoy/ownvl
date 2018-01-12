from urllib.parse import urlparse, parse_qs

class Rays:

    def fetch(self, raysData):
        
        for val in raysData['media$content']:
            if val['plfile$format'] != "M3U":
                continue

            sourceURL = val['plfile$sourceUrl']

            res = parse_qs(urlparse(sourceURL).query)
            rays_raw = res['rays'][0]
            rays_letters = rays_raw.split(':')[2][:-1]
            
            return list(rays_letters)

        return []