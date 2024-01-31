import os
import matplotlib
import geopandas
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from shapely.geometry import Point, Polygon
from PIL import Image as Image
import base64

Image.MAX_IMAGE_PIXELS = None

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.shp') or f.endswith('geojson'):
            print (f)
            fName = len(f)
            filePath = os.path.join(dirName, f)
            metadata = os.path.join(dirName, f + '.xml')
            tree = ET.parse(metadata)
            root = tree.getroot()
            thumbnail = root.find('Binary/Thumbnail/Data')
            vector = geopandas.read_file(filePath)
            vector.plot()
            plot = vector.plot()
            plot.set_axis_off()
            fig = plot.get_figure()
            fig.savefig(filePath[:-fName] + 'preview.jpg')
            outputfile = filePath[:-fName] + 'preview.jpg'
            with open(outputfile, "rb") as image:
                b64string = base64.b64encode(image.read())
                thumbnail.text = str(b64string)[2:]
                tree.write(metadata)
        elif f.endswith('.tif'):
            print (f)
            fName = len(f)
            filePath = os.path.join(dirName, f)
            metadata = os.path.join(dirName, f + '.xml')
            tree = ET.parse(metadata)
            root = tree.getroot()
            thumbnail = root.find('Binary/Thumbnail/Data')
            outputfile = filePath[:-fName] + 'preview.jpg'
            im = Image.open(filePath)
            if im.mode in ('RGBA', 'P') or im.mode in ('RGBX', 'P'):
                im = im.convert('RGB')
                datas = im.getdata()
                new_image_data = []
                for item in datas:
                    if item[0] in list(range(0, 1)):
                        new_image_data.append((255, 255, 255))
                    else:
                        new_image_data.append(item)       
                im.putdata(new_image_data)
                im.thumbnail((128, 128), Image.LANCZOS)
            im.save(outputfile, 'JPEG')
            with open(outputfile, 'rb') as image:
                b64string = base64.b64encode(image.read())
                thumbnail.clear()
                thumbnail.text = str(b64string)[2:]
                tree.write(metadata)
