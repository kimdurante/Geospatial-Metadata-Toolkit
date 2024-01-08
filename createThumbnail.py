import os
import matplotlib
import geopandas
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from shapely.geometry import Point, Polygon
from PIL import Image as Image
import base64


for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.shp'):
            filePath = os.path.join(dirName, f)
            print (f[:-4])
            metadata = os.path.join(dirName, f + '.xml')
            tree = ET.parse(metadata)
            root = tree.getroot()
            thumbnail = root.find('Binary/Thumbnail/Data')
            shapefile = geopandas.read_file(filePath)
            shapefile.plot()
            plot = shapefile.plot()
            plot.set_axis_off()
            fig = plot.get_figure()
            fig.savefig(filePath[:-4] + '.jpg')
            outputfile = os.path.join(dirName, f[:-4] + '.jpg')
            with open(outputfile, "rb") as image:
                b64string = base64.b64encode(image.read())
                thumbnail.text = str(b64string)[2:]
                tree.write(metadata)
                os.remove(outputfile)
        elif f.endswith('.tif'):
            print (f)
            filePath = os.path.join(dirName, f)
            metadata = os.path.join(dirName, f + '.xml')
            tree = ET.parse(metadata)
            root = tree.getroot()
            thumbnail = root.find('Binary/Thumbnail/Data')
            outputfile = filePath[:-4] + '.jpg'
            im = Image.open(filePath)
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
                datas = im.getdata()
                new_image_data = []
                for item in datas:
                    if item[0] in list(range(0, 1)):
                        new_image_data.append((255, 255, 255))
                    else:
                        new_image_data.append(item)       
                im.putdata(new_image_data)
                im.thumbnail((128, 128), Image.ANTIALIAS)
            im.save(outputfile, "JPEG")
            with open(outputfile, "rb") as image:
                b64string = base64.b64encode(image.read())
                thumbnail.clear()
                thumbnail.text = str(b64string)[2:]
                tree.write(metadata)
                os.remove(outputfile)
