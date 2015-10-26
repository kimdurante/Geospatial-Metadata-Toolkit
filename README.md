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

| ISO Element       | GeoBlacklight  | Entry Method  |
| ------------- |:-------------:| -----:|
| Title      | dc_title_s | Free text |
| ResponsibleParty (CI_RoleCode='originator') |dc_creator_sm| Controlled vocabulary |
| Date | dct_isseud_s     | Date w3cdtf |
| Responsible Party (CI_RoleCode =’publisher’) | dc_publisher_sm   | Controlled vocabulary |
| Abstract | dc_description | Free text |
| Dataset Identifier | uuid | URI |
| ISO Topic Category | dc_subject_sm | ISO Codelist |
| Theme keyword(s) | dc_subject_sm | Controlled vocabulary |
| Place keyword(s) | dc_spatial_sm | Controlled vocabulary |
| Temporal extent | dc_temporal_sm/solr_year_i | Date(s) w3cdtf |
| Access/Use Constraints | dc_rights_s | ISO Codelist |
| Distributor | dct_provenance_s | Contact template |
| Metadata date stamp | layer_modified_dt | Date w3cdtf |
| Distribution format | dc_format_s | Controlled vocabulary (local) |
| Language | dc_language_sm | ISO Codelist |
| Aggregate Dataset Name |dc_isPartOf_sm  | Free text |
| Hierarchy level | dc_type_s | ISO Codelist |
| Geographic extent | georss_box_s | W,E,N,S decimal degrees |
| Hierarchy level | dc_type_s | ISO Codelist |
| Hierarchy level | dc_type_s | ISO Codelist |
| Metadata file identifier | dct_references | Text (uuid or namespace authority + identifier |
| Spatial reference |  | EPSG Code |
| Metadata contact |  | Contact template |



