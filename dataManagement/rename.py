#this script reads through a directory of files and replaces any value specified in 'chars' with an underscore '_'
import os
chars = ['&','-',' ','%','(',')','^']

for dirName, subDirs, fileNames in os.walk('.'):
   for f in fileNames:
      f = os.path.join(dirName, f)
      for sc in chars:
         if sc in f:
            os.rename(f, f.replace(sc, '_'))
