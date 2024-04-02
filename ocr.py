from PIL import Image
import pytesseract
import numpy as np
import os

os.environ['TESSDATA_PREFIX'] = '/opt/conda/share/tessdata'
pytesseract.pytesseract.tesseract_cmd = r'/opt/conda/bin/tesseract'
filename = '1_python-ocr.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)