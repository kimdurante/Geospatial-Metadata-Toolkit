# geoMetadata
XML templates, XSLTs, and Python scripts, for working with geospatial metadata in ISO 19139 and 19110 formats.

### XSLT

updateISO.xsl

This XSL can be used for items that already have pre-existing metadata that need to be normalized. It also adds institutional level metadata, such as distributor information and thesauri citations. The example provided in the variables is from the National Atlas of the United States. The top-level variables can be replaced according to specific collection needs.

### Python

addISO.py

This script adds identifiers to ISO 19139 metadata records, including metadata file identifier, citation URL, and distribution URL. A UUID for feature catalogs can also be added, if applicable.

addAttrs.py

This script reads through a csv of attribute definitions and creates an ISO 19110 record using the FC_template.xml document.

### XML Templates

SUL_template.xml 

This is an ISO 19139 template for Stanford University. This template can be used for creating new metadata records.

FC_template.xml

This is a very basic template for collecting ISO 19110 metadata for the description of feature catalogs. Each attribute must have a name (LABEL) and a definition element. If attribute definitions/codelists are provided in a .csv file, see addAttrs.py to automate creating of these metadata using this template.

{| class="wikitable"
|-
! Header 1
! Header 2
! Header 3
|-
| row 1, cell 1
| row 1, cell 2
| row 1, cell 3
|-
| row 2, cell 1
| row 2, cell 2
| row 2, cell 3
|}

