from bottle import route, request, run
from components.extract import *

@route('/')
def hello_world():
    return 'Hello from the otherside!!'


@route('/parse', method="POST")
def parse_image():
    fil = request.files.get("image")
    print(fil.file)
    return {
            "coupon_id": "New",
            "company_name": "Dummy",
            "description": "50% off"
        }

    ocr = OCR()
    text = ocr.extract("test.png")
    print(text)


run(host='localhost', port=8080)
