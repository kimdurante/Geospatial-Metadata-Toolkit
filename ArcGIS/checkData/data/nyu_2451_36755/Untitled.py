from osgeo import ogr, osr
driver = ogr.GetDriverByName('ESRI Shapefile')
dataset = driver.Open(r'ags_entidad.shp')

# from Layer
layer = dataset.GetLayer()
##spatialRef = layer.GetSpatialRef()
# from Geometry
feature = layer.GetNextFeature()
geom = feature.GetGeometryRef()
spatialRef = geom.GetSpatialReference()

print spatialRef
