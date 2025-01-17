# Applies an ArcGISXML template to all layers in a directory. Reads a csv of metadata values and writes them to the matching elements.

import xml.etree.ElementTree as ET
import os
from datetime import datetime
import time
import csv

template = 'template.xml'

# Dictionary of ISO Topic Categories
isotopics = {'farming': '001','biota': '002','boundaries': '003','climatologyMeteorologyAtmosphere' : '004','economy' : '005','elevation' : '006', 'environment': '007','geoscientificInformation' : '008', 'health' : '009', 'imageryBaseMapsEarthCover':'010', 'intelligenceMilitary':'011','inlandWaters':'012','location':'013','oceans':'014','planningCadastre':'015','society':'016','structure':'017', 'transportation':'018','utilitiesCommunication':'019' }

# Dictionary of Update Frequencies
frequencies = {'continual': '001','daily': '002','weekly': '003','fortnightly' : '004','monthly' : '005','quarterly' : '006', 'biannually': '007','annually' : '008', 'asNeeded' : '009', 'irregular':'010', 'notPlanned':'011','unknown':'012'}
# Create dictionary from 'metadata.csv.' Skip the header row
metadict = {}
reader = csv.reader(open('metadata.csv', 'r'))
next(reader)

for rows in reader:
    metadict[rows[0]] = rows[2], rows[3], rows[4], rows[5].split('|'), rows[6].split('|'), rows[7].split('|'), rows[8], rows[9], rows[10].split('|'), rows[11].split('|'), rows[12].split('|'), rows[13].split('|'), rows[14], rows[15], rows[16].split('|'), rows[17], rows[18], rows[19], rows[20], rows[21], rows[22], rows[23], rows[24], rows[25], rows[26]

def applyTemplate():
    tree = ET.parse(template)
    root = tree.getroot()
    new_file = filePath + '.xml'
    tree.write(new_file)


def addMetadata():
    for k, v in metadict.items():
        if k + '.xml' == f:
            print (tempPeriod.text)
            distName.text = k
            URL.text = 'https://purl.stanford.edu/' + v[0]
            dataSetURI.text = 'https://purl.stanford.edu/' + v[0]
            distURL.text = 'https://purl.stanford.edu/' + v[0]
            metadataId.text = 'edu.stanford.purl:' + v[0]
            resTitle.clear()
            resTitle.text = v[1]
            abstract.text = v[2]
            if v[3] == '':
                orig.remove(originatorInd)
            else:
                originatorInd.text = v[3][0]
            if v[4] == '':
                orig.remove(originatorOrg)
            else:
                originatorOrg.text = v[4][0]
            if (v[3][0] == '') and (v[4][0] == ''):
                idCitation.remove(orig)
            publisher.text = v[5][0]
            publicationDate = datetime.strptime(v[6], '%m/%d/%y')
            publicationDate = datetime.strftime(publicationDate,'%Y-%m-%dT%H:%M:%S')
            pubDate.text = publicationDate
            if v[7] == '':
                idCitation.remove(edition)
            else:
                edition.text = v[7]
            for isotopic, isocode in isotopics.items():
                 if v[8][0] == isotopic:
                     topicCategory[0].set('value', isocode)
                 for index, tpCat in enumerate(v[8][0:]):
                     newElem = ET.Element('tpCat') 
                     if index > 0:
                         if tpCat == isotopic:
                             tpCatIndex = list(dataIdInfo).index(topicCategory)
                             dataIdInfo.insert(tpCatIndex +1, newElem)
                             newIsoCat = ET.SubElement(newElem, 'TopicCatCd')
                             newIsoCat.set('value', isocode)
            themeKey.text = v[9][0]
            placeKey.text = v[10][0]
            for index, theme in enumerate(v[9][0:]):
                if index > 0:
                    themeKeys.insert(index, ET.Element('keyword'))
                    themeKeys[index].text = theme
            for index, place in enumerate(v[10][0:]):
                if index > 0:
                    placeKeys.insert(index, ET.Element('keyword'))
                    placeKeys[index].text = place
                   
            if v[11][0] == '':
                tempInstant.text = publicationDate
                dataExt.remove(dataExt[2])
                exDesc.text = 'publication date'
            else:    
                try:
                    (v[11][1])
                    temporalBeg = datetime.strptime(v[11][0], '%m/%d/%Y')
                    temporalBeg = datetime.strftime(temporalBeg,'%Y-%m-%dT%H:%M:%S')
                    temporalEnd = datetime.strptime(v[11][1], '%m/%d/%Y')
                    temporalEnd = datetime.strftime(temporalEnd,'%Y-%m-%dT%H:%M:%S')
                    tempPeriod[0].text = temporalBeg
                    tempPeriod[1].text = temporalEnd
                    dataExt.remove(dataExt[1])
                    print (tempPeriod[0].text, tempPeriod[1].text)
                except IndexError: 
                    temporalInst = datetime.strptime(v[11][0], '%m/%d/%y')
                    temporalInst = datetime.strftime(temporalInst,'%Y-%m-%dT%H:%M:%S')
                    tempInstant.text = temporalInst
                    print (tempInstant.text)
                    dataExt.remove(dataExt[2])

            for freq, freqcode in frequencies.items():
                if v[12] == freq:
                    updateFreq.set('value', freqcode)

            fileFormat.text = v[13]
            language[0].set('value', v[14][0])
            for index, lang in enumerate(v[14][0:]):
                if index > 0:
                    language.insert(index, ET.Element('dataLang'))
                    newLang = ET.SubElement(language, 'languageCode')
                    newLang.set('value', lang)

            if v[15] == '':
                contInfo.remove(featureCatalog)
            else:
                fcId.text = v[15]

            collectionTitle.text = v[16]
            aggrDSTitle.text = v[16]
            aggrDSId.text = 'https://purl.stanford.edu/' + v[17]
            parentMetadataId.text = 'https://purl.stanford.edu/' + v[17] + '.mods'
            if v[18] == 'public':
                accessConsts.remove(access)
            usage.text = v[19]

            if v[20] == '':
                pointOfContact.remove(contactInd)
            else:
                contactInd.text = v[20]
            if v[21] == '':
                pointOfContact.remove(contactOrg)
            else:
                contactOrg.text = v[21]
            if v[22] == '':
                pointOfContact.remove(contactEmail)
            else:
                contactEmail.text = v[22]
            if v[20] == '' and v[21] == '':
                dataIdInfo.remove(pointOfContact)
            dataSourceTitle.text = v[23]
            dataSourceId.text = v[24]
            if (v[23] == ''):
                sourceCitation.remove(sourceCitation[0])
                
            
                        
    
#Walk through the directory and find shapefiles, create an XML document.
for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.endswith('.shp') or f.endswith('.tif'):
            filePath = os.path.join(dirName, f)
            applyTemplate()

#Find elements and insert metadata values.
        if f.endswith('.shp.xml') or f.endswith('tif.xml'):
            filePath = os.path.join(dirName, f)
            print (f)
            tree = ET.parse(filePath)
            root = tree.getroot()
            dataIdInfo = root.find('dataIdInfo')
            metadataId = root.find('mdFileID')
            parentMetadataId = root.find('mdParentID')
            dataSetURI = root.find('dataSetURI')
            resTitle = root.find('dataIdInfo/idCitation/resTitle')
            abstract = root.find('dataIdInfo/idAbs')
            placeKeys = root.find('dataIdInfo/placeKeys')
            placeKey = root.find('dataIdInfo/placeKeys/keyword')
            themeKeys = root.find('dataIdInfo/themeKeys')
            themeKey = root.find('dataIdInfo/themeKeys/keyword')
            topicCategory = root.find('dataIdInfo/tpCat')
            pubDate = root.find('dataIdInfo/idCitation/date/pubDate')
            edition = root.find('dataIdInfo/idCitation/resEd')
            contactName = root.find('dataIdInfo/idPoC/rpOrgName')
            address = root.find('dataIdInfo/idPoC/rpCntInfo/cntAddress/eMailAdd')
            dataExt = root.find('dataIdInfo/dataExt')
            tempInstant = root.find('dataIdInfo/dataExt/tempEle/TempExtent/exTemp/TM_Instant/tmPosition')
            tempPeriod = root.find('dataIdInfo/dataExt/tempEle/TempExtent/exTemp/TM_Period')
            exDesc = root.find('dataIdInfo/dataExt/exDesc')
            fileFormat = root.find('distInfo/distFormat/formatName')
            distURL = root.find('distInfo/distTranOps/onLineSrc/linkage')
            distName = root.find('distInfo/distTranOps/onLineSrc/orName')
            URL = root.find('dataIdInfo/idCitation/citId/identCode')
            contInfo = root.find('contInfo')
            featureCatalog = root.find('contInfo/FetCatDesc')
            fcId = root.find('contInfo/FetCatDesc/catCitation/citId/identCode')
            aggrDSTitle = root.find('dataIdInfo/aggrInfo/aggrDSName/resTitle')
            aggrDSId = root.find('dataIdInfo/aggrInfo/aggrDSName/citId/identCode')
            collectionTitle = root.find('dataIdInfo/idCitation/collTitle')
            rightsText = root.find('dataIdInfo/resConst/LegConsts/othConsts')
            idCitation = root.find('dataIdInfo/idCitation')
            orig = root.find('dataIdInfo/idCitation/citRespParty[2]')
            originatorOrg = root.find('dataIdInfo/idCitation/citRespParty[2]/rpOrgName')
            originatorInd = root.find('dataIdInfo/idCitation/citRespParty[2]/rpIndName')
            pub = root.find('dataIdInfo/idCitation/citRespParty[1]')
            publisher = root.find('dataIdInfo/idCitation/citRespParty[1]/rpOrgName')
            language = root.find('dataIdInfo/dataLang')
            dataIdInfo = root.find('dataIdInfo')
            pointOfContact = root.find('dataIdInfo/idPoC')
            contactInd = root.find('dataIdInfo/idPoC/rpIndName')
            contactOrg = root.find('dataIdInfo/idPoC/rpOrgName')
            contactEmail = root.find('dataIdInfo/idPoC/rpCntInfo/cntAddress/eMailAdd')
            updateFreq = root.find('dataIdInfo/resMaint/maintFreq/MaintFreqCd')
            accessConsts = root.find('dataIdInfo/resConst/LegConsts/accessConsts')
            access = root.find('dataIdInfo/resConst/LegConsts/accessConsts/RestrictCd')
            usage = root.find('dataIdInfo/resConst/LegConsts/othConsts')
            sourceCitation = root.find('dqInfo/dataLineage')
            dataSourceTitle = root.find('dqInfo/dataLineage/dataSource/srcCitatn/resTitle')
            dataSourceId = root.find('dqInfo/dataLineage/dataSource/srcCitatn/citId/identCode')
            addMetadata()
            tree.write(filePath)       
