#Synchronize Metadata (arc_sync_md.py). Walk through a directory of shapefiles and GeoTIFFs, and update the metadata.
import arcpy
from arcpy import env
from arcpy import metadata as md
import os

#Path to the data directory
env.workspace = "W:\PATH_TO_DIRECTORY"

for dirs, subdirs, files in os.walk(env.workspace):
    for f in files:
        if f.endswith(".shp") or f.endswith(".tif"):
            filePath = os.path.join(dirs, f)
            src_item_md = md.Metadata(filePath)
            print (src_item_md)
            src_item_md.synchronize("ALWAYS")
