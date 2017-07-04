##  This script scans a directory of shapefiles and TIFFs and prints out some data properties for each layer
##
##
##westBC = minx
##eastBC = maxx
##northBC = maxy
##southBC = miny


from osgeo import gdal, osr, ogr
import os

datasets = []

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.shp'):
            print f
            f = os.path.join(dirName, f)
            ds = ogr.Open(f)
            for lyr in ds:
                (minx, maxx, miny, maxy) = lyr.GetExtent()
                #datasets.append(lyr.GetExtent)              
                print("Geometry type: %s" % ogr.GeometryTypeToName(lyr.GetGeomType()))
                srs = lyr.GetSpatialRef()
                srsAuth = srs.GetAttrValue("AUTHORITY",0)
                srsCode = srs.GetAttrValue("AUTHORITY",1)
                if srsAuth is not None:
                   print 'Projection is: '+ srsAuth + '::' + srsCode
                else:
                   print 'Projection is missing!'
                print 'Extent : %f, %f - %f %f' % (minx, miny, maxx, maxy)
                print '\n'
                                

        if f.endswith ('.tif'):
            print f
            f = os.path.join(dirName, f)
            ds = gdal.Open(f)
            width = ds.RasterXSize
            height = ds.RasterYSize
            gt = ds.GetGeoTransform()
            minx = gt[0]
            miny = gt[3] + width*gt[4] + height*gt[5]
            maxx = gt[0] + width*gt[1] + height*gt[2]
            maxy = gt[3]
            prj = ds.GetProjection()
            srs=osr.SpatialReference(wkt=prj)
            if srs.IsProjected:
                srs = srs.GetAttrValue('authority', 0) + '::' + srs.GetAttrValue('authority', 1)
            
            print 'Raster Type: ', ds.GetDriver().ShortName,'/', \
                  ds.GetDriver().LongName
            print 'Size is ',ds.RasterXSize,'x',ds.RasterYSize, \
                  'x',ds.RasterCount
            print 'Projection is: ' + srs
                  
            print 'Extent : %f, %f - %f %f' % (minx, miny, maxx, maxy)
            print '\n'

