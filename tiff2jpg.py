import os
import xml.etree.ElementTree as ET
import PIL.Image
from PIL import Image as Image
import io
import base64
import warnings
PIL.Image.MAX_IMAGE_PIXELS = 933120000

warnings.simplefilter('ignore', Image.DecompressionBombWarning)

def createJPEG():
    tiff_name = os.path.join(dirName, f)
    metadata = os.path.join(dirName, f + '.xml')
    tree = ET.parse(metadata)
    root = tree.getroot()
    thumbnail = root.find('Binary/Thumbnail/Data') 
    outputfile = tiff_name[:-4] + '.jpg'
    im = Image.open(tiff_name).convert('RGB')
    im.thumbnail((128, 128), Image.ANTIALIAS)
    im.save(outputfile, "JPEG")
    with open(outputfile, "rb") as image:
        b64string = base64.b64encode(image.read())
        thumbnail.clear()
        thumbnail.text = str(b64string)[2:]
        print (thumbnail.text)
        tree.write(metadata)
                
for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.startswith('.'):
            continue
        if f.endswith('TIF') or f.endswith('.tif'):
            createJPEG()
