 import os 

#invalid characters
chars = ['&','-',' ','%','(',')','^']

# Function to rename multiple files 
def rename(f):
    filePath = os.path.join(dirName, f)
    for sc in chars:
        if sc in f:
            copy_f = filePath.replace(sc, '')
            print (copy_f)
            os.rename(filePath,copy_f)

#search directory recursively
for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        rename(f)
