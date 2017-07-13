import csv
import os
import xml.etree.ElementTree as ET


metadict = {}
reader = csv.reader(open("metadata.csv", "rU"))
for rows in reader:
    filename = rows[0]
    title = rows[1]
    identifier = rows[2]
    uuid = rows[3]
    metadict[filename] = identifier, title

originator = 'AUTHOR(S). '
publisher = 'PUBLISHER'   

def createMetadata():
    print f
    for k, v in metadict.items():
        if v[1] == title:
           metadataID.text = 'edu.stanford.purl:' + v[0]
           URL.text = 'http//purl.stanford.edu/' + v[0]
           distURL.text = 'http//purl.stanford.edu/' + v[0]
           distName.text = k
           URI.text = 'http//purl.stanford.edu/' + v[0]

def createCitation():
    credit.text = originator + '(' + pubDate + '). ' + title + '. ' + publisher + '. Available at: ' + URL.text + '.'
    print credit.text

    
for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith("shp.xml"):
            print f
            file = os.path.join(dirName, f)  
            tree = ET.parse(file)
            root = tree.getroot()
            metadataID = root.find('mdFileID')
            ResTitle = root.find('dataIdInfo/idCitation/resTitle').text
            pubDate = root.find('dataIdInfo/idCitation/date/pubDate').text
            pubDate = pubDate[:4]
            distURL = root.find('distInfo/distTranOps/onLineSrc/linkage')
            distName = root.find('distInfo/distTranOps/onLineSrc/orName')
            URL = root.find('dataIdInfo/idCitation/citId/identCode')
            fcID = root.find('contInfo/FetCatDesc/catCitation/citId/identCode')
            URI = root.find('dataSetURI')
            fcTitle = root.find ('contInfo/FetCatDesc/catCitation/resTitle')
            credit = root.find('dataIdInfo/idCredit')
            fcTitle.clear()
            fcTitle.text = 'Feature catalog for ' + ResTitle
            fcID.clear()
            fcID.text = uuid
            credit.clear()
            createMetadata()
            createCitation()

            print URL.text
  #         tree.write(file)
              
