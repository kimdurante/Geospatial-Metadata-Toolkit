import csv
import os
import sys
import xml.etree.ElementTree as ET
namespaces = {'gmd': 'http://www.isotc211.org/2005/gmd','gco': 'http://www.isotc211.org/2005/gco', 'gml': 'http://www.opengis.net/gml', 'gmx':'http://www.isotc211.org/2005/gmx','gfc': 'http://www.isotc211.org/2005/gfc'}

attributes = {}
reader = csv.reader(open("attributes.csv", "rU"))
for rows in reader:
    label = rows[0]
    definition = rows[1]
    attributes[label] = definition    

ISO19139_file = sys.argv[-1]
ISO19110_file = ISO19139_file[:-4] + '_fc.xml'

tree = ET.parse(ISO19139_file)
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
title = root.find('gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString', namespaces=namespaces).text
date = root.find('gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date', namespaces=namespaces).text

open(ISO19110_file, 'w')
tree = ET.parse('fc_template.xml')
root = tree.getroot()
featureType = root.find('gfc:featureType/gfc:FC_FeatureType', namespaces=namespaces)
featureName = root.find('gfc:featureType/gfc:FC_FeatureType/gfc:typeName/gco:LocalName', namespaces=namespaces)
fc_title = root.find('gmx:name/gco:CharacterString', namespaces=namespaces)
fc_date = root.find('gmx:versionDate/gco:Date', namespaces=namespaces)
fc_title.text = title
fc_date.text = date[:4]


for k,v in attributes.items():
    featureType.insert(4,ET.Element('{http://www.isotc211.org/2005/gfc}carrierOfCharacteristics'))
    featureAttribute = ET.SubElement(featureType[4],'{http://www.isotc211.org/2005/gfc}FC_FeatureAttribute')
    memName = ET.SubElement(featureType[4][0],'{http://www.isotc211.org/2005/gfc}memberName')
    locName = ET.SubElement(featureAttribute[0],'{http://www.isotc211.org/2005/gco}LocalName')
    locName.text = k
    attr = ET.SubElement(featureType[4][0],'{http://www.isotc211.org/2005/gfc}definition')
    definition = ET.SubElement(attr,'{http://www.isotc211.org/2005/gco}CharacterString')
    definition.text = v
    cardinality = ET.SubElement(featureType[4][0],'{http://www.isotc211.org/2005/gfc}cardinality')
    cardinality.set('gco:nilReason','unknown')
#   print (definition.text)



##    multiplicity = ET.SubElement(cardinality,'{http://www.isotc211.org/2005/gco}Multiplicity')
##    attrRange = ET.SubElement(multiplicity,'{http://www.isotc211.org/2005/gco}range')
##    mulRange = ET.SubElement(attrRange,'{http://www.isotc211.org/2005/gco}MultiplicityRange')
##    lowRange = ET.SubElement(mulRange,'{http://www.isotc211.org/2005/gco}lower')
##    lowRange.set('gco:nilReason', 'unknown')
##    upRange = ET.SubElement(mulRange,'{http://www.isotc211.org/2005/gco}upper')
##    upRange.set('gco:nilReason', 'unknown')
    

    tree.write(ISO19110_file)

                