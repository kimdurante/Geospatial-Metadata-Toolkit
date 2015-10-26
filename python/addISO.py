import csv
import os
import xml.etree.ElementTree as ET
namespaces = {'gmd': 'http://www.isotc211.org/2005/gmd','gco': 'http://www.isotc211.org/2005/gco', 'gml': 'http://www.opengis.net/gml', 'gfc': 'http://www.isotc211.org/2005/gfc'}

if __name__=="__main__":
    metadict = {}
    reader = csv.reader(open("identifiers.csv", "rU"))
    for rows in reader:
        filename = rows[0]
        druid = rows[1]
        layerTitle = rows[2]
        metadict[filename] = druid, layerTitle

#for credit statement generation
author = 'Hart Energy Publishing'
publisher = 'Hart Energy Publishing'
pubdate = '2007'


for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('metadata.xml'):
            file = os.path.join(dirName, f)
            #print file
            tree = ET.parse(file)
            root = tree.getroot()
            ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
            ET.register_namespace('gmd', 'http://www.isotc211.org/2005/gmd')
            ET.register_namespace('gco', 'http://www.isotc211.org/2005/gco')
            ET.register_namespace('gts', 'http://www.isotc211.org/2005/gts')
            ET.register_namespace('gss', 'http://www.isotc211.org/2005/gss')
            ET.register_namespace('gsr', 'http://www.isotc211.org/2005/gsr')
            ET.register_namespace('gfc', 'http://www.isotc211.org/2005/gfc')
            ET.register_namespace('gmx', 'http://www.isotc211.org/2005/gmx')
            ET.register_namespace('gmi', 'http://www.isotc211.org/2005/gmi')
            ET.register_namespace('gml', 'http://www.opengis.net/gml')
            title = root.find('gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString', namespaces=namespaces)
            credit = root.find('gmd:identificationInfo/gmd:MD_DataIdentification/gmd:credit/gco:CharacterString', namespaces=namespaces)
            metadataID = root.find('gmd:fileIdentifier/gco:CharacterString', namespaces=namespaces)
            URL = root.find('gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:identifier/gmd:MD_Identifier/gmd:code/gco:CharacterString', namespaces=namespaces)
            URI = root.find('gmd:dataSetURI/gco:CharacterString', namespaces=namespaces)
            distURL = root.find('gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL', namespaces=namespaces)
            distName = root.find('gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:name/gco:CharacterString',  namespaces=namespaces)
            for k, v in metadict.items():
                if v[1] == title.text:
                   #metadataID.text = 'edu.stanford.purl:' + v[0]
                   URL.text = 'http//purl.stanford.edu/' + v[0]
                   distURL.text = 'http//purl.stanford.edu/' + v[0]
                   distName.text = k
                   credit.text = author + '. ' + title.text + '(' + pubdate + '). ' + publisher + '. Available at: http//purl.stanford.edu/' + v[0] + '.'
                   print URL.text
                   tree.write(file)
            
                    
                
