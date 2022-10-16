from bottle import ServerAdapter, server_names, route, post, request, run
from socket import gethostname


@route('/')
def hello_world():
    return 'Hello from the otherside!!'


@route('/parse', method="POST")
def parse_image():
    fil = request.files.get("image")
    print(fil.file)
    return {
            "coupon_code": "New",
            "company": "Dummy",
            "text": "50% off"
        }


run(host='localhost', port=8080)
