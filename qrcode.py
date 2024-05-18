import pyqrcode
from PIL import Image

qr_kod = pyqrcode.create("https://www.linkedin.com/in/kemal-altu%C4%9F-k%C4%B1l%C4%B1n%C3%A7-8a9372251/")
cikti = "qr_kod.png"
qr_kod.png(cikti,scale=10)
cerceve = Image.open(cikti)
cerceve.show()
