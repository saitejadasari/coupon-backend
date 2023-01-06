from extract import *

ocr = OCR()
text = ocr.extract("../images/coupon.png")
print(text)
