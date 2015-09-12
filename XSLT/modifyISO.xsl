<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:gco="http://www.isotc211.org/2005/gco" 
    xmlns:gmi="http://www.isotc211.org/2005/gmi"
    xmlns:gmd="http://www.isotc211.org/2005/gmd" 
    xmlns:gml="http://www.opengis.net/gml"
    exclude-result-prefixes="gml gmd gco gmi xsl">
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="no"/>
    <xsl:strip-space elements="*"/>

    <!-- copy all metadata conent -->
    <xsl:template match="node() | @*">
        <xsl:copy>
            <xsl:apply-templates select="node() | @*"/>
        </xsl:copy>
    </xsl:template>

    <!-- set variables -->
    <xsl:variable name="collTitle">The National Atlas of the United States</xsl:variable>
    <xsl:variable name="collURL">http://purl.stanford.edu/cv275yx9215</xsl:variable>   
    <xsl:variable name="collDate">2010-12-31</xsl:variable>
    <xsl:variable name="rights"><xsl:text>This item is in the public domain.</xsl:text></xsl:variable>
    <xsl:variable name="originator"><xsl:text>National Atlas of the United States</xsl:text></xsl:variable>
    
    <xsl:variable name="title">
        <xsl:value-of select="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString"/>
    </xsl:variable>

    <xsl:variable name="pubdate">
        <xsl:value-of
            select="substring(//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date,1,4)"/>
    </xsl:variable>

    <xsl:template match="gmd:identificationInfo/gmd:MD_DataIdentification/gmd:credit"/>
    <xsl:template match="gmd:fileIdentifier"/>
    <xsl:template match="gmd:MD_Metadata">
        <xsl:copy>
            <gmd:fileIdentifier>
                <gco:CharacterString>METADATA_ID</gco:CharacterString>
            </gmd:fileIdentifier>
            <xsl:apply-templates select="*"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="gmd:contact">
        <xsl:copy>
            <xsl:apply-templates select="node() | @*"/>
        </xsl:copy>
        <gmd:contact>
            <gmd:CI_ResponsibleParty>
                <xsl:copy-of select="document('contact.xml')//gmd:CI_ResponsibleParty/gmd:organisationName | document('contact.xml')//gmd:CI_ResponsibleParty/gmd:individualName"/> 
        <xsl:copy-of select="document('contact.xml')//gmd:contactInfo"/>
        <gmd:role>
            <gmd:CI_RoleCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_RoleCode" codeListValue="pointOfContact" codeSpace="ISOTC211/19115">pointOfContact</gmd:CI_RoleCode>
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
      
    <xsl:template match="gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:date">
        <xsl:copy>
            <xsl:apply-templates select="node() | @*"/>
        </xsl:copy>
        <gmd:identifier>
            <gmd:MD_Identifier>
                <gmd:code>
                    <gco:CharacterString>URL</gco:CharacterString>
                </gmd:code>
            </gmd:MD_Identifier>
        </gmd:identifier>
    </xsl:template>
    
    <xsl:template match="gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation">
        <xsl:copy>
            <xsl:apply-templates select="node() | @*"/>

        <gmd:collectiveTitle>
            <gco:CharacterString><xsl:value-of select="$collTitle"/></gco:CharacterString>
        </gmd:collectiveTitle>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="gmd:identificationInfo/gmd:MD_DataIdentification/gmd:purpose">
        <xsl:copy>
            <xsl:apply-templates select="node() | @*"/>
        </xsl:copy>
        <gmd:credit>
            <gco:CharacterString>
                <xsl:text>National Atlas of the United States. (</xsl:text>
                <xsl:value-of select="$pubdate"/>
                <xsl:text>). </xsl:text>
                <xsl:value-of select="$title"/>
                <xsl:text>. </xsl:text>
                <xsl:text>National Atlas of the United States.</xsl:text>
            </gco:CharacterString>
        </gmd:credit>
    </xsl:template>

    <!-- add thesauri citations -->
    <!--lcsh -->
    <xsl:template match="gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords">
        <xsl:choose>
            <xsl:when test="contains(gmd:type/gmd:MD_KeywordTypeCode[@codeListValue], 'theme')">
                <gmd:MD_Keywords>
                    <xsl:copy-of select="ancestor-or-self::*/gmd:keyword"/>
                    <xsl:copy-of select="ancestor-or-self::*/gmd:type"/>
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
                                        <gmd:CI_DateTypeCode
                                            codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode"
                                            codeListValue="revision" codeSpace="ISOTC211/19115"
                                            >revision</gmd:CI_DateTypeCode>
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
            </xsl:when>

<!-- geonames -->
            <xsl:when test="contains(gmd:type/gmd:MD_KeywordTypeCode[@codeListValue], 'place')">
                <gmd:MD_Keywords>
                    <xsl:copy-of select="ancestor-or-self::*/gmd:keyword"/>
                    <xsl:copy-of select="ancestor-or-self::*/gmd:type"/>
                    <gmd:thesaurusName>
                        <gmd:CI_Citation>
                            <gmd:title>
                                <gco:CharacterString>geonames</gco:CharacterString>
                            </gmd:title>
                            <gmd:date>
                                <gmd:CI_Date>
                                    <gmd:date>
                                        <gco:Date>2012-11-01</gco:Date>
                                    </gmd:date>
                                    <gmd:dateType>
                                        <gmd:CI_DateTypeCode
                                            codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode"
                                            codeListValue="revision" codeSpace="ISOTC211/19115"
                                            >revision</gmd:CI_DateTypeCode>
                                    </gmd:dateType>
                                </gmd:CI_Date>
                            </gmd:date>
                            <gmd:identifier>
                                <gmd:MD_Identifier>
                                    <gmd:code>
                                        <gco:CharacterString>http://www.geonames.org/ontology#</gco:CharacterString>
                                    </gmd:code>
                                </gmd:MD_Identifier>
                            </gmd:identifier>
                        </gmd:CI_Citation>
                    </gmd:thesaurusName>
                </gmd:MD_Keywords>
            </xsl:when>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="gmd:resourceConstraints[2]">
        <gmd:resourceConstraints>
            <gmd:MD_LegalConstraints>
                <gmd:useLimitation>
                    <gco:CharacterString><xsl:value-of select="$rights"/></gco:CharacterString>
                </gmd:useLimitation>
            </gmd:MD_LegalConstraints>
        </gmd:resourceConstraints>  
       <gmd:aggregationInfo>
            <gmd:MD_AggregateInformation>
                <gmd:aggregateDataSetName>
                    <gmd:CI_Citation>
                        <gmd:title>
                            <gco:CharacterString><xsl:value-of select="$collTitle"/></gco:CharacterString>
                        </gmd:title>
                        <gmd:date>
                            <gmd:CI_Date>
                                <gmd:date>
                                    <gco:Date><xsl:value-of select="$collDate"></xsl:value-of></gco:Date>
                                </gmd:date>
                                <gmd:dateType>
                                    <gmd:CI_DateTypeCode
                                        codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode"
                                        codeListValue="publication" codeSpace="ISOTC211/19115">publication</gmd:CI_DateTypeCode>
                                </gmd:dateType>
                            </gmd:CI_Date>
                        </gmd:date>
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
    </xsl:template>       
    
    <!-- change the distributor information -->

    <xsl:template match="gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor">
        <gmd:distributor>
        <gmd:MD_Distributor>
            <gmd:distributorContact>
                <gmd:CI_ResponsibleParty>
                <xsl:copy-of select="document('contact.xml')//gmd:CI_ResponsibleParty/gmd:organisationName"/> 
                <xsl:copy-of select="document('contact.xml')//gmd:contactInfo"/>
                    <gmd:role>
                        <gmd:CI_RoleCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_RoleCode" codeListValue="distributor" codeSpace="ISOTC211/19115">distributor</gmd:CI_RoleCode>
                    </gmd:role>
                </gmd:CI_ResponsibleParty>
            </gmd:distributorContact>
        </gmd:MD_Distributor>
        </gmd:distributor>
    </xsl:template>

    <xsl:template match="gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions">
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
                    <gmd:function>
                        <gmd:CI_OnLineFunctionCode
                            codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_OnLineFunctionCode"
                            codeListValue="download" codeSpace="ISOTC211/19115">download</gmd:CI_OnLineFunctionCode>
                    </gmd:function>
                </gmd:CI_OnlineResource>
            </gmd:onLine>
        </gmd:MD_DigitalTransferOptions>
    </xsl:template>

</xsl:stylesheet>
