try:
     import Image
except ImportError:
     from PIL import Image
import pytesseract
print("image", pytesseract.image_to_string(Image.open("C:/Users/bearb/3.jpg")))
print("image", pytesseract.image_to_string(Image.open("C:/Users/bearb/Dropbox/School/Grad School Work/DoIE/InteractiveDND/RaspiPython/image.jpg")))
print("done")