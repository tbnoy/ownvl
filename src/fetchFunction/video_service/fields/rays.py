from urllib.parse import urlparse, parse_qs

class Rays:

    def fetch(self, raysData):
        
        for val in raysData['media$content']:
            if val['plfile$format'] != "M3U":
                continue

            sourceURL = val['plfile$sourceUrl']

            # sourceURL :
            # https://content.uplynk.com/ext/682389d3b3e244a5bd4b9853036d1eff/CDF001B001B.m3u8?rays={param:rays:abcdefg}&hlsver=5&tc=1&exp={date:90}&rn={n}&ct=a&eid=CDF001B001B&oid=682389d3b3e244a5bd4b9853036d1eff&euid={param:bbuidHash}{param:bbuid}&platform={param:platform}&platformDetail={param:platformDetail}&sig={hmac:HmacSHA256:/CTg1LY+3/AU6vBO6k4eSiO3khqViVQKzH1brRlF::::true}

            res = parse_qs(urlparse(sourceURL).query)
            rays_raw = res['rays'][0]
            rays_letters = rays_raw.split(':')[2][:-1]
            
            return list(rays_letters)

        return []