import csv
import xml.etree.ElementTree as ET
import os
import csv
baseD = os.getcwd()
output_file = open( 'NTA.csv', 'w' )
##data = csv.reader(open('france2.csv', "rU"))
##for line in data:
##    filename = (line[0])
##    subject = (line[1])
    

for dirName, subDirs, fileNames in os.walk(os.getcwd()):
    for f in fileNames:
        if f.endswith("shp.xml") or f.endswith('tif.xml') or f.endswith ('metadata.xml'):
            filePath = os.path.join(dirName, f)
            print (f)
            tree = ET.parse(filePath)
            root = tree.getroot()
            #layerName = root.find('Esri/DataProperties/itemProps/itemName').text
            placeKey = root.find("dataIdInfo/placeKeys/keyword")
            resTitle = root.find("dataIdInfo/idCitation/resTitle").text
            #resTitle = str(resTitle)
            #resTitle = str(resTitle.encode('utf-8'))
            location = root.find('Esri/DataProperties/itemProps/itemLocation/linkage').text
            location = str(location)
            location = str(location.encode('utf-8'))
            print (f)
            output_file.write(f + ',' + '"' + resTitle + '"' + ',' + '\n')


                    
                            # idC = root.find('dataIdInfo/idCitation')
#                           idC.getchildren()
                            
                            #identCode = ET.SubElement(citID,'identCode')
                            #tree.write(f)       
                            #print parentID.text                
                            
                            
                            
                            
                            
                           
                            
                    
                 #   print layerN  
                
                           

                    
                
                    

                #print filePath
#                       with open(filePath, 'r'):
#                               tag = root.find('mdFileID').text

                                
                # print f       
#                       print layerName         
                        
#             #print layerName
#             
                    
                                        


#open the XML files for reading, register namespaces, insert fileidentifer element    

        #filePath = os.path.join('.', f)
        

#             
        
#inserts the element and charString         
            #root.insert(0, ET.Element('gmd:fileIdentifier'))
            #gco = ET.SubElement(root[0], 'gco:CharacterString')
            
#write csv cell to fileID element           
            #gco.text = (line[1])
            #tree.write(layerName)
            
            
# #writes the feature catalog identifier into a uuidref attribute of the featureCatalogCitation     
#           for content in root.iter('{http://www.isotc211.org/2005/gmd}featureCatalogueCitation'):
#                  content.clear()
#                  content.set('uuidref',line[3])
#                  tree.write(layerName)
            
        
        

                


        
        
        
        
    
