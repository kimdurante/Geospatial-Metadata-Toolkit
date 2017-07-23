#this script reads through a directory of files and replaces any value specified in 'chars' with an underscore '_'
import os
chars = ['&','-',' ','%','(',')','^']


for dirName, subDirs, fileNames in os.walk('.'):
   for f in fileNames:
      f = os.path.join(dirName, f)
      copy_f = f 
      for sc in chars:
         if sc in copy_f:
            copy_f = copy_f.replace(sc, '_')
      os.rename(f,copy_f)
