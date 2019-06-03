#!/bin/bash

# script_dir="$(dirname $0)"
# html_dir="${script_dir}/../build_output"


########### Build lab_manual
cd lab_manual
## Lint the XML
xmllint --valid lab_manual.xml --noout
## Render the HTML
ant webhelp

# TODO Copy to directory
# cp -r lab_manual/data build_output/lab_manual
# cd ..

########## Shove in grc_doc
#TODO Shove in grc_doc
# mkdir build_output/grc_doc
# cp -r grc_doc/build_output/* build_output/grc_doc

########## Add static site elements
# TODO Shove in index.html and grc_doc
cp static_site/index.html build_output