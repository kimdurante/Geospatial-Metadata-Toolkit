<?xml version="1.0" encoding="UTF-8"?>
<!-- this stylesheet will normalize existing metadata to conform to ISO standards. Use set variables to apply collection-level metadata to indiviudual ISO 19139 records. 
This docuemnt uses the 'contact.xml' docuemnt to add Responsible party information. -->
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:gco="http://www.isotc211.org/2005/gco" 
    xmlns:gmi="http://www.isotc211.org/2005/gmi"
    xmlns:gmd="http://www.isotc211.org/2005/gmd" 
    xmlns:gml="http://www.opengis.net/gml"
    exclude-result-prefixes="gml gmd gco gmi xsl">
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="no"/>
    <xsl:strip-space elements="*"/>
     
    <!-- copy all metadata conent -->
    
    <xsl:template match="/">
        <xsl:apply-templates select="node() | @*"/>
    </xsl:template>
    
    <xsl:template match="node() | @*" priority="0">
        <xsl:copy>
            <xsl:apply-templates select="node() | @*"/>
        </xsl:copy>
    </xsl:template>
    
    <!-- set variables -->
    <xsl:variable name="collTitle">The National Atlas of the United States</xsl:variable>
    <xsl:variable name="collURL">http://purl.stanford.edu/cv275yx9215</xsl:variable>
    <xsl:variable name="otherCitationDetails">These data were downloaded from the National Atlas website on August 15, 2014.</xsl:variable>
    
    <xsl:variable name="title">
        <xsl:value-of select="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString"/>
    </xsl:variable>
    
    <xsl:variable name="pubdate">
        <xsl:value-of
            select="substring(//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date,1,4)"/>
    </xsl:variable>
    <xsl:template match="gmd:MD_Metadata">
        <xsl:copy>
            <gmd:fileIdentifier>
                <gco:CharacterString>METADATA_ID</gco:CharacterString>
            </gmd:fileIdentifier>
            <xsl:apply-templates select="*"/>
        </xsl:copy>

    </xsl:template>    
    <xsl:template match="gmd:contact[1]">
    <xsl:copy-of select="."/>
        <gmd:contact>
            <gmd:CI_ResponsibleParty>
                <gmd:individualName gco:nilReason="missing">
                    <gco:CharacterString />
                </gmd:individualName>
                <gmd:organisationName>
                    <gco:CharacterString>Stanford Geospatial Center</gco:CharacterString>
                </gmd:organisationName>
                <gmd:positionName gco:nilReason="missing">
                    <gco:CharacterString />
                </gmd:positionName>
                <gmd:contactInfo>
                    <gmd:CI_Contact>
                        <gmd:phone>
                            <gmd:CI_Telephone>
                                <gmd:voice gco:nilReason="missing">
                                    <gco:CharacterString />
                                </gmd:voice>
                                <gmd:facsimile gco:nilReason="missing">
                                    <gco:CharacterString />
                                </gmd:facsimile>
                            </gmd:CI_Telephone>
                        </gmd:phone>
                        <gmd:address>
                            <gmd:CI_Address>
                                <gmd:deliveryPoint>
                                    <gco:CharacterString>Branner Earth Sciences Library</gco:CharacterString>
                                </gmd:deliveryPoint>
                                <gmd:city>
                                    <gco:CharacterString>Stanford</gco:CharacterString>
                                </gmd:city>
                                <gmd:administrativeArea>
                                    <gco:CharacterString>California</gco:CharacterString>
                                </gmd:administrativeArea>
                                <gmd:postalCode>
                                    <gco:CharacterString>94305</gco:CharacterString>
                                </gmd:postalCode>
                                <gmd:country>
                                    <gco:CharacterString>United States of America</gco:CharacterString>
                                </gmd:country>
                                <gmd:electronicMailAddress>
                                    <gco:CharacterString>brannerlibrary@stanford.edu</gco:CharacterString>
                                </gmd:electronicMailAddress>
                            </gmd:CI_Address>
                        </gmd:address>
                    </gmd:CI_Contact>
                </gmd:contactInfo>
                <gmd:role>
                    <gmd:CI_RoleCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_RoleCode" codeListValue="pointOfContact" />
                </gmd:role>
            </gmd:CI_ResponsibleParty>
        </gmd:contact>
    </xsl:template>
    
    <xsl:template match="gmd:MD_Metadata/gmd:characterSet">
        <xsl:copy>
            <xsl:apply-templates select="*"/>
        </xsl:copy>
        <gmd:parentIdentifier>
            <gco:CharacterString><xsl:value-of select="$collURL"/><xsl:text>.mods</xsl:text></gco:CharacterString>
        </gmd:parentIdentifier>
    </xsl:template>
    
    <xsl:template match="gmd:MD_Metadata/gmd:metadataStandardVersion">
        <xsl:copy>
            <xsl:apply-templates select="*"/>
        </xsl:copy>
        <gmd:dataSetURI><gco:CharacterString>PURL</gco:CharacterString></gmd:dataSetURI>
    </xsl:template>
    
    <xsl:template match="gmd:identificationInfo/gmd:MD_DataIdentification">
        <gmd:MD_DataIdentification> 
        <xsl:for-each select="gmd:citation">   
        <gmd:citation>
        <gmd:CI_Citation>
            <xsl:apply-templates select="gmd:CI_Citation/gmd:title"/>

            <xsl:apply-templates select="gmd:CI_Citation/gmd:date"/>
            
            <gmd:identifier>
                <gmd:MD_Identifier>
                    <gmd:code>
                        <gco:CharacterString>URL</gco:CharacterString>
                    </gmd:code>
                </gmd:MD_Identifier>
            </gmd:identifier>
            <xsl:apply-templates select="gmd:CI_Citation/gmd:citedResponsibleParty"/>
            <xsl:apply-templates select="gmd:CI_Citation/gmd:presentationForm"/>
            <gmd:otherCitationDetails>
                <gco:CharacterString><xsl:value-of select="$otherCitationDetails"/></gco:CharacterString>
            </gmd:otherCitationDetails>
            <gmd:collectiveTitle>
                <gco:CharacterString><xsl:value-of select="$collTitle"/></gco:CharacterString>
            </gmd:collectiveTitle>
        </gmd:CI_Citation>
            </gmd:citation>
        </xsl:for-each>
        <xsl:apply-templates select="gmd:abstract"/>
        <xsl:apply-templates select="gmd:purpose"/>
        <gmd:credit>
            <gco:CharacterString>CREDIT</gco:CharacterString>
        </gmd:credit>
    
    <!-- add thesauri citations -->
    <!--lcsh -->
        <xsl:for-each select="gmd:descriptiveKeywords">
         <xsl:choose>
            <xsl:when test="contains(gmd:MD_Keywords/gmd:type/gmd:MD_KeywordTypeCode[@codeListValue], 'theme')">
                <gmd:descriptiveKeywords>
                   <gmd:MD_Keywords>
                <xsl:copy-of select="ancestor-or-self::*/gmd:MD_Keywords/gmd:keyword"/>
                <gmd:type>
                    <gmd:MD_KeywordTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode" codeListValue="theme">theme</gmd:MD_KeywordTypeCode>
                </gmd:type>
                       <gmd:thesaurusName>
                           <gmd:CI_Citation>
                               <gmd:title>
                                   <gco:CharacterString>lcsh</gco:CharacterString>
                               </gmd:title>
                               <gmd:date>
                                   <gmd:CI_Date>
                                       <gmd:date>
                                           <gco:Date>2011-04-26</gco:Date>
                                       </gmd:date>
                                       <gmd:dateType>
                                           <gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode"
                                               codeListValue="revision"
                                               codeSpace="ISOTC211/19115">revision</gmd:CI_DateTypeCode>
                                       </gmd:dateType>
                                   </gmd:CI_Date>
                               </gmd:date>
                               <gmd:identifier>
                                   <gmd:MD_Identifier>
                                       <gmd:code>
                                           <gco:CharacterString>http://id.loc.gov/authorities/subjects.html</gco:CharacterString>
                                       </gmd:code>
                                   </gmd:MD_Identifier>
                               </gmd:identifier>
                           </gmd:CI_Citation>
                       </gmd:thesaurusName>
                    </gmd:MD_Keywords>
                </gmd:descriptiveKeywords>
            </xsl:when>
        
             <xsl:when test="contains(gmd:MD_Keywords/gmd:type/gmd:MD_KeywordTypeCode[@codeListValue], 'place')">
                 <gmd:descriptiveKeywords>
                     <gmd:MD_Keywords>
                    <xsl:copy-of select="ancestor-or-self::*/gmd:MD_Keywords/gmd:keyword"/>
                    <gmd:thesaurusName>
                        <gmd:CI_Citation>
                            <gmd:title>
                                <gco:CharacterString>lcnaf</gco:CharacterString>
                            </gmd:title>
                            <gmd:date>
                                <gmd:CI_Date>
                                    <gmd:date>
                                        <gco:Date>2011-04-26</gco:Date>
                                    </gmd:date>
                                    <gmd:dateType>
                                        <gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode"
                                            codeListValue="revision"
                                            codeSpace="ISOTC211/19115">revision</gmd:CI_DateTypeCode>
                                    </gmd:dateType>
                                </gmd:CI_Date>
                            </gmd:date>
                            <gmd:identifier>
                                <gmd:MD_Identifier>
                                    <gmd:code>
                                        <gco:CharacterString>http://id.loc.gov/authorities/names.html</gco:CharacterString>
                                    </gmd:code>
                                </gmd:MD_Identifier>
                            </gmd:identifier>
                        </gmd:CI_Citation>
                    </gmd:thesaurusName>
                </gmd:MD_Keywords>
            </gmd:descriptiveKeywords>
        </xsl:when>
</xsl:choose>
        </xsl:for-each>
        <xsl:apply-templates select="gmd:resourceConstraints"/>
        <gmd:aggregationInfo>
            <gmd:MD_AggregateInformation>
                <gmd:aggregateDataSetName>
                    <gmd:CI_Citation>
                        <gmd:title>
                            <gco:CharacterString><xsl:value-of select="$collTitle"/></gco:CharacterString>
                        </gmd:title>
                        <gmd:identifier>
                            <gmd:MD_Identifier>
                                <gmd:code>
                                    <gco:CharacterString><xsl:value-of select="$collURL"/></gco:CharacterString>
                                </gmd:code>
                            </gmd:MD_Identifier>
                        </gmd:identifier>
                    </gmd:CI_Citation>
                </gmd:aggregateDataSetName>
                <gmd:associationType>
                    <gmd:DS_AssociationTypeCode
                        codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#DS_AssociationTypeCode"
                        codeListValue="largerWorkCitation" codeSpace="ISOTC211/19115">largerWorkCitation</gmd:DS_AssociationTypeCode>
                </gmd:associationType>
                <gmd:initiativeType>
                    <gmd:DS_InitiativeTypeCode
                        codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#DS_InitiativeTypeCode"
                        codeListValue="collection" codeSpace="ISOTC211/19115">collection</gmd:DS_InitiativeTypeCode>
                </gmd:initiativeType>
            </gmd:MD_AggregateInformation>
        </gmd:aggregationInfo>      
        </gmd:MD_DataIdentification>
    </xsl:template>
    <!-- change the distributor information -->
    
    <xsl:template match="gmd:distributionInfo/gmd:MD_Distribution">
        <gmd:distributor>
            <gmd:MD_Distributor>
                <gmd:distributorContact>
                    <gmd:CI_ResponsibleParty>
                        <gmd:organisationName>
                            <gco:CharacterString>Stanford Geospatial Center</gco:CharacterString>
                        </gmd:organisationName>
                        <gmd:contactInfo>
                            <gmd:CI_Contact>
                                <gmd:phone>
                                    <gmd:CI_Telephone>
                                        <gmd:voice>
                                            <gco:CharacterString>650-723-2746</gco:CharacterString>
                                        </gmd:voice>
                                    </gmd:CI_Telephone>
                                </gmd:phone>
                                <gmd:address>
                                    <gmd:CI_Address>
                                        <gmd:deliveryPoint>
                                            <gco:CharacterString>Branner Earth Sciences Library</gco:CharacterString>
                                        </gmd:deliveryPoint>
                                        <gmd:deliveryPoint>
                                            <gco:CharacterString>Mitchell Building, 2nd Floor</gco:CharacterString>
                                        </gmd:deliveryPoint>
                                        <gmd:deliveryPoint>
                                            <gco:CharacterString>397 Panama Mall</gco:CharacterString>
                                        </gmd:deliveryPoint>
                                        <gmd:city>
                                            <gco:CharacterString>Stanford</gco:CharacterString>
                                        </gmd:city>
                                        <gmd:administrativeArea>
                                            <gco:CharacterString>California</gco:CharacterString>
                                        </gmd:administrativeArea>
                                        <gmd:postalCode>
                                            <gco:CharacterString>94305</gco:CharacterString>
                                        </gmd:postalCode>
                                        <gmd:country>
                                            <gco:CharacterString>United States of America</gco:CharacterString>
                                        </gmd:country>
                                        <gmd:electronicMailAddress>
                                            <gco:CharacterString>brannerlibrary@stanford.edu</gco:CharacterString>
                                        </gmd:electronicMailAddress>
                                    </gmd:CI_Address>
                                </gmd:address>
                            </gmd:CI_Contact>
                        </gmd:contactInfo>
                        <gmd:role>
                            <gmd:CI_RoleCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_RoleCode" codeListValue="distributor" />
                        </gmd:role>
                    </gmd:CI_ResponsibleParty>
                </gmd:distributorContact>
                <gmd:distributorFormat>
                    <gmd:MD_Format>
                        <gmd:name>
                            <gco:CharacterString>Shapefile</gco:CharacterString>
                        </gmd:name>
                        <gmd:version gco:nilReason="missing">
                            <gco:CharacterString />
                        </gmd:version>
                    </gmd:MD_Format>
                </gmd:distributorFormat>
            </gmd:MD_Distributor>
        </gmd:distributor>

        <gmd:MD_DigitalTransferOptions>
            <gmd:onLine>
                <gmd:CI_OnlineResource>
                    <gmd:linkage>
                        <gmd:URL>URL</gmd:URL>
                    </gmd:linkage>
                    <gmd:protocol>
                        <gco:CharacterString>http</gco:CharacterString>
                    </gmd:protocol>
                    <gmd:name>
                        <gco:CharacterString>FILENAME</gco:CharacterString>
                    </gmd:name>
                </gmd:CI_OnlineResource>
            </gmd:onLine>
        </gmd:MD_DigitalTransferOptions>
    </xsl:template>
</xsl:stylesheet>
