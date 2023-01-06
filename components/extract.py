from pytesseract import pytesseract


class OCR:

    def __init__(self):
        self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        print("initialization")

    def extract(self, test):

        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(test)
            return text

        except Exception as e:
            print(e)
            return "Error"

