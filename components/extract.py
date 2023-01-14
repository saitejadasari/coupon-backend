from pytesseract import pytesseract
import cv2


class OCR:

    def __init__(self):
        self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        print("initialization")

    def extract(self, image):
        try:
            pytesseract.tesseract_cmd = self.path

            boxes_list = []
            # Detecting words
            img = cv2.imread(image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            hImg, wImg, _ = img.shape
            data = pytesseract.image_to_data(img)
            # print("image to data", data)
            for count, b in enumerate(data.splitlines()):
                if count != 0:
                    b = b.split()
                    if len(b) == 12:
                        boxes_list.append(b)

            return boxes_list

        except Exception as e:
            print(e)
            return "Error"

    def extract_and_show(self, image):
        try:
            pytesseract.tesseract_cmd = self.path

            # Detecting text
            # text = pytesseract.image_to_string(image)

            boxes_list = []
            # Detecting words
            img = cv2.imread(image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            hImg, wImg, _ = img.shape
            data = pytesseract.image_to_data(img)
            # print("image to data", data)
            for count, b in enumerate(data.splitlines()):
                if count != 0:
                    b = b.split()
                    if len(b) == 12:
                        boxes_list.append(b)
                        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                        cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
                        cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

            cv2.imshow("Result", img)
            cv2.waitKey(0)
            return boxes_list

        except Exception as e:
            print(e)
            return "Error"
