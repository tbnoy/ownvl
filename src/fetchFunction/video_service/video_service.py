from fetchFunction.feed_data.factories import getPlatform
from fetchFunction.feed_data.factories import getProfileApi
from .fields_decider import fieldsDecider
from fetchFunction.feed_data.platform_feed import PlatformFeed
from .fields.metadata import Metadata
from .fields.modifiers import Modifiers
from .fields.captions import Captions
from .fields.rays import Rays
from .fields.thumbnail import Thumbnail
from .fields.urls import Urls
from .fields.ads import Ads
from .fields.audio import Audio
from .fields.auth import Auth
from .fields.waivers import Waivers


class VideoService:

    def __init__(self):
        self.baseData = {}
        self.raysData = {}
        self.language = "english"

    def fetch(self, params): 
        response = {}

        platformFeed = getPlatform()
        
        res = platformFeed.fetchBase(params['videoGuid'])
        
        self.baseData = res

        res = platformFeed.fetchRays(params['videoGuid'])
        self.raysData = res
        
        fields = fieldsDecider(params['fields'].split(","))
        
        if 'metadata' in fields:
            metadata = Metadata()
            response["metadata"] = metadata.fetch(self.baseData)

        if 'urls' in fields:
            urls = Urls()
            response["urls"] = urls.fetch(self.baseData, self.raysData, params['profileGuid'], params['platform'])

        if 'modifiers' in fields:
            modifiers = Modifiers(platformFeed)
            response["modifiers"] = modifiers.fetch(self.baseData)
        
        if 'captions' in fields:
            captions = Captions()
            response["captions"] = captions.fetch(self.raysData)

        if 'rays' in fields:
            rays = Rays()
            response["rays"] = rays.fetch(self.raysData)

        if 'auth' in fields:
            auth = Auth(getProfileApi())
            response["auth"] = auth.fetch(self.baseData, self.raysData, params, self.language)
        
        if 'waivers' in fields:
            waivers = Waivers(getProfileApi())
            response["waivers"] = waivers.fetch(self.baseData, self.raysData, params, self.language)
        
        if 'thumbnail' in fields:
            thumbnail = Thumbnail()
            response["thumbnail"] = thumbnail.fetch(self.baseData)

        if 'audio' in fields:
            audio = Audio()
            response["audio"] = audio.fetch(self.raysData)

        if 'ads' in fields:
            ads = Ads()
            response["ads"] = ads.fetch(self.baseData, params['profileGuid'], params['platform'])
            

        return response