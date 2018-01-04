from chalice import Chalice, Response
from video_service import VideoService

app = Chalice(app_name='fetchFunction')
app.debug = True

# http://localhost:8000/v1/data/CDF001B001B?profileguid=5F5DA2E8-D4EF-45FA-AB7B-F49A6A3226DE&platform=web&fields=metadata

@app.route('/')
def index():
    return notFound()

@app.route('/v1/data/{videoGuid}')
def index(videoGuid):
    requestParams = app.current_request.query_params

    params = {
        "videoGuid": videoGuid,
        "profileGuid": requestParams.get("profileguid"),
        "platform": requestParams.get("platform"),
        "fields": requestParams.get("fields")
    }
    fields = params['fields']    
    
    try:
        videoService = VideoService()
        res = videoService.fetch(params)
    except BaseException as ex:
        print("ex: ")
        print(ex)
        return notFound()
    
    return respond(res)

def respond(res):
    return {
        "code": 200,
        "status": "success",
        "data": res
    }

def notFound():
    return Response(
        body={
            "detail": "Video Not Found",
            "code": 1000
        },
        status_code=404
    )

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
