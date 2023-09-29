import os
from osgeo import ogr
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import base64


for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.shp'):
            f = os.path.join(dirName, f)
            ds = ogr.Open(f)
            nlay = ds.GetLayerCount()
            lyr = ds.GetLayer()
            print (lyr, f)
            ext = lyr.GetExtent()
            xoff = (ext[1]-ext[0])/50
            yoff = (ext[3]-ext[2])/50
            print (yoff)
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.set_xlim(ext[0]-xoff,ext[1]+xoff)
            ax.set_ylim(ext[2]-yoff,ext[3]+yoff)
            paths = []
            lyr.ResetReading()
            for feat in lyr:
                geom = feat.geometry()
                codes = []
                all_x = []
                all_y = []
                for i in range(geom.GetGeometryCount()):
                    r = geom.GetGeometryRef(i)
                    x = [r.GetX(j) for j in range(r.GetPointCount())]
                    y = [r.GetY(j) for j in range(r.GetPointCount())]
                    #codes += [mpath.Path.MOVETO] + (len(x)-1)*[mpath.Path.LINETO]
                    #print (codes)
                    all_x += x
                    all_y += y
                    print (all_x, all_y)
                path = mpath.Path(np.column_stack((all_x,all_y)))
                paths.append(path)
            for path in paths:
                patch = mpatches.PathPatch(path, \
                        facecolor='#FFFFCC', edgecolor='black')
                ax.add_patch(patch)
            for spine in plt.gca().spines.values():
                spine.set_visible(False)
            plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False)    
            plt.savefig(f[:-4] + '.jpg')
            #ax.set_aspect(1.0)
            #plt.show()
            with open(f[:-4] + '.jpg', "rb") as imageFile:
                str = base64.b64encode(imageFile.read())
                print (str)
                
