from PIL import Image
import pytesseract

file = '1.png'
text = pytesseract.image_to_string(Image.open(file))
print(text)