from osgeo import gdal, osr, ogr

import os
import csv

#Create a csv of filenames and spatial reference systems (SRS), and data types.

output_file = open( 'data.csv', 'w' )
headers = ['filename', 'spatial reference','type' ]
writer = csv.writer(output_file)
writer.writerow(headers)

#Find shapefiles in a directory. Open the data and get the SRS and the geometry type.

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.shp'):
            print ('Filename: ' + f)
            filePath = os.path.join(dirName, f)
            ds = ogr.Open(filePath)
            for lyr in ds:
                srs = lyr.GetSpatialRef()
                try:
                   srs
                   srsAuth = srs.GetAttrValue('AUTHORITY',0)
                   srsCode = srs.GetAttrValue('AUTHORITY',1)
                   #print (f)
                except:
                    srsAuth = 'NONE'
                    srsCode = 'NONE' 
                    print ('Missing Spatial Reference ' + f)
                geomType = ogr.GeometryTypeToName(lyr.GetGeomType())
            output_file.write(f + ',' + srsCode + ',' + geomType + '\n')

 #Find geotiffs and get the SRS            
        else:
            if f.endswith('.tif'):     
                f = os.path.join(dirName, f)
                ds = gdal.Open(f)
                prj = ds.GetProjection()
                srs=osr.SpatialReference(wkt=prj)
                
                try:
                    srs
                    if srs.IsProjected:
                        #print (f)
                        srs = srs.GetAttrValue('authority', 0) + '::' + srs.GetAttrValue('authority', 1)
                        srsAuth =srs[4:]
                        srsCode =srs[6:]
                except:
                    srsAuth = 'NONE'
                    srsCode = 'NONE'
                    print ('Missing spatial reference ' +f)        
                output_file.write(f + ',' + srsCode + ',' + 'GeoTIFF' + '\n')            

output_file.close()              
