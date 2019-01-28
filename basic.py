from PIL import Image
from pytesseract import *

def tesseract(imgfile, lang = 'kor'):
    im = Image.open(imgfile)
    text = image_to_string(im, lang=lang)

    print('Letis go ocr result')
    print(text)

tesseract('ocr_test.jpg')
#OCR('koream_ocr_test.png',lang='kor')
