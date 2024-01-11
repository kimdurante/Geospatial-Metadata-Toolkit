import xml.etree.cElementTree as ET
import shutil
import os
import csv

if __name__=="__main__":
    folders = {}
    reader = csv.reader(open("metadata.csv", "rU"))
    for rows in reader:
        filename = rows[0]
        filename = filename.split('.')[0]
        druid = rows[8]
        folders[filename] = druid
 

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.shp') or f.endswith('.shp.xml') or f.endswith('.shx') or f.endswith('.dbf') or f.endswith('.cpg') or f.endswith('.prj') or f.endswith('.sbn'):
            filePath = os.path.join(dirName, f)
            fileN = f.split('.')[0]
            for k, v in folders.items():
                k = k.split('.')[0]
                if fileN == k:
                    print (filePath)
                    newdir = r"/Volumes/METADATA/California_Tuolumne_County/2023"
                    druiddir = os.path.join(newdir,v)
                    movedir = os.path.join(druiddir, 'temp')
                    print (movedir)
                    shutil.copy2(filePath, movedir)
