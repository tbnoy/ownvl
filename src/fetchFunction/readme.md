# Module Docs

## Brief
This module is used by other services, currently serverless framework with AWS.

It use the main module that handles the calls: `VideoService`

## Components

### config/conf
Simply gets the environment variables and stores it in a dict for other components to access.

### feed_data/
##### factories
In charge of creating the: `platform` and `profile` apis with all the proper configs.

#### platform_feed
Fetches data for base video data and rays video data.

#### ProfileApi
Fetches data for user profile and waivers data.

### video_service/
##### fields_decider
The function handles the filtering and deciding for fields to fetch by api input.

##### video_service
In charge for fetching the base data from the other components and fetching the proper data for each field requested.

##### /fields/
This folder holds all the fields that may be requested, and each component handles itself with the proper inputs.

###### /fields/ads
loads another smil file by specific value from base data and parses the needed values.

###### /fields/audio
loads another file by base data, parses and returns.

###### /fields/auth
loads auth data by using `profileApi` from above

###### /fields/captions
parses rays data for captions

###### /fields/metadata
parses base data for metadata

###### /fields/modifiers
fetch more videos with `platformFeed` from base data inputs

###### /fields/rays
parses rays data specific value url

###### /fields/thumbnail
parses base data for thumbnails

###### /fields/urls
parses base data and preps urls

###### /fields/waivers
loads waivers data by using `profileApi` from above