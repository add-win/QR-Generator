import qrcode
import qrcode.constants
from PIL import Image,ImageDraw
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data('Website URL')
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
draw=ImageDraw.Draw(img)
img.save('qr.png')