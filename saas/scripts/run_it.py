
import urllib
from PIL import Image
from io import BytesIO
import base64
f = open('base64.txt', 'r')
data = f.read()
data = urllib.unquote(data)
print data
im = Image.open(BytesIO(base64.b64decode(data)))
im.save("foo.png")


