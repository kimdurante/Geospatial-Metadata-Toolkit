import xml.etree.cElementTree as ET
import shutil
import os
import csv


folders = {}
reader = csv.reader(open("metadata.csv", "rU"))
for rows in reader:
    filename = rows[0]
    filename = filename.split('.')[0]
    druid = rows[2]
    folders[filename] = druid
 

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.tif') or f.endswith('.tif.xml') or f.endswith('.prj') or f.endswith('.tfw'):
            filePath = os.path.join(dirName, f)
            fileN = f.split('.')[0]
            for k, v in folders.items():
                k = k.split('.')[0]
                if fileN == k:
                    print (f)
                    newdir = r"R:\METADATA\NGA_Nautical_Charts"
                    druiddir = os.path.join(newdir,v)
                    movedir = os.path.join(druiddir, 'temp')
                    print (movedir)
                    shutil.copy2(filePath, movedir)
