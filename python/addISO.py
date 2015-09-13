#This script will read through a csv of filenames and identifiers and write values into ISO XML
import csv
import os
import xml.etree.ElementTree as ET
namespaces = {'gmd': 'http://www.isotc211.org/2005/gmd','gco': 'http://www.isotc211.org/2005/gco', 'gml': 'http://www.opengis.net/gml', 'gfc': 'http://www.isotc211.org/2005/gfc'}

with open('identifiers.csv', 'rU') as IDs:
    reader = csv.DictReader(IDs)
    identifiers = {(line['filename']): line['druid'] for line in reader }     

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.xml'):
            file = os.path.join(dirName, f)
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
            metadataID = root.find('gmd:fileIdentifier/gco:CharacterString', namespaces=namespaces)
            URL = root.find('gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:identifier/gmd:MD_Identifier/gmd:code/gco:CharacterString', namespaces=namespaces)
            distName = root.find('gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:name/gco:CharacterString', namespaces=namespaces)
            URI = root.find('gmd:dataSetURI/gco:CharacterString', namespaces=namespaces)
            distURL = root.find('gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL', namespaces=namespaces)
            fcID = root.find('gmd:contentInfo/gmd:MD_FeatureCatalogueDescription/gmd:featureCatalogueCitation/gmd:CI_Citation/gmd:identifier/gmd:MD_Identifier/gmd:code/gco:CharacterString',namespaces=namespaces)  
            for filename, druid in identifiers.items():
                p = filename[:-4]
                if p + '.xml' == f:
                   metadataID.text = 'edu.stanford.purl:' + druid
                   URL.text = 'http//purl.stanford.edu/' + druid
                   distURL.text = 'http//purl.stanford.edu/' + druid
                   distName.text = filename
                   print metadataID.text
                tree.write(file)
            
                    
                
