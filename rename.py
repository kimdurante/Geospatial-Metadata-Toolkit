## This script scans a directory of files and removes any characters in filenames which are not letters, numbers, or underscores. ##

import os
import re

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        oldFilename = os.path.join(dirName, f)
        f  = re.sub('[^A-Za-z0-9._]+', '', f)
        newFilename = os.path.join(dirName, f)
        print (oldFilename, newFilename)
        os.rename(oldFilename, newFilename)
