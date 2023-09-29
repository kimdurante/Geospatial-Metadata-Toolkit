import csv
import os
import xml.etree.ElementTree as ET

attrdict = {}
reader = csv.reader(open("attrs.csv", "rU"))
for rows in reader:
    for rows in reader:
        label = rows[0]
        definition = rows[1]
        attrdict[label] = definition

print attrdict
for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.xml'):
            file = os.path.join(dirName, f)
            tree = ET.parse(file)
            root = tree.getroot()
            atts = root.findall('eainfo/detailed/attr')
            alabel = root.findall('eainfo/detailed/attr/attrlabl')
            ascale = root.findall('eainfo/detailed/attr/attscale')

            for i in atts:
                label = i[0].text
                i.insert(6,ET.Element('attrdef'))
                for k,v in attrdict.items():
                    #print k, v
                    if label == k:
                       i[6].text = v
                       print (label, i[6].text)
  #                     tree.write(file)


                
