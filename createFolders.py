import csv, os

data = csv.reader(open('metadata.csv', 'rU'))

os.chdir('.')
for line in data:
    os.mkdir(line[1])

for root, dirs, files in os.walk('.'):
	
    for d in dirs:
        os.chdir(d)
        os.mkdir('temp')
        os.chdir('..')
     
        
        
 	    
 

    
    





          
