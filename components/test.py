from extract import *

ocr = OCR()
text = ocr.extract("../images/coupon.png")
text = ocr.extract_and_show("../images/coupon.png")
print(text)
