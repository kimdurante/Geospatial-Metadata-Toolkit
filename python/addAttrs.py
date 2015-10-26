import csv
import os
import xml.etree.ElementTree as ET
namespaces = {'gmd': 'http://www.isotc211.org/2005/gmd','gco': 'http://www.isotc211.org/2005/gco', 'gml': 'http://www.opengis.net/gml', 'gfc': 'http://www.isotc211.org/2005/gfc'}

if __name__=="__main__":
    attrdict = {}
    reader = csv.reader(open("attributes.csv", "rU"))
    for rows in reader:
        label = rows[0]
        definition = rows[1]
        attrdict[label] = definition   

tree = ET.parse('fcAGEB.xml')
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
featureType = root.find('gfc:featureType/gfc:FC_FeatureType', namespaces=namespaces)
for k,v in attrdict.items():
    featureType.insert(3,ET.Element('{http://www.isotc211.org/2005/gfc}carrierOfCharacteristics'))
    featureAttribute = ET.SubElement(featureType[3],'{http://www.isotc211.org/2005/gfc}FC_FeatureAttribute')
    memName = ET.SubElement(featureType[3][0],'{http://www.isotc211.org/2005/gfc}memberName')
    locName = ET.SubElement(featureAttribute[0],'{http://www.isotc211.org/2005/gco}LocalName')
    attr = ET.SubElement(featureType[3][0],'{http://www.isotc211.org/2005/gfc}definition')
    definition = ET.SubElement(attr,'{http://www.isotc211.org/2005/gco}CharacterString')
    cardinality = ET.SubElement(featureType[3][0],'{http://www.isotc211.org/2005/gfc}cardinality')
    multiplicity = ET.SubElement(cardinality,'{http://www.isotc211.org/2005/gco}Multiplicity')
    attrRange = ET.SubElement(multiplicity,'{http://www.isotc211.org/2005/gco}range')
    mulRange = ET.SubElement(attrRange,'{http://www.isotc211.org/2005/gco}MultiplicityRange')
    lowRange = ET.SubElement(mulRange,'{http://www.isotc211.org/2005/gco}lower')
    lowRange.set('gco:nilReason', 'unknown')
    upRange = ET.SubElement(mulRange,'{http://www.isotc211.org/2005/gco}upper')
    upRange.set('gco:nilReason', 'unknown')
    locName.text = k
    definition.text = v
    print definition.text
    tree.write('fcAGEB.xml')
