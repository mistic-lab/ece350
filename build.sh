#!/bin/bash

# script_dir="$(dirname $0)"
# html_dir="${script_dir}/../build_output"


########### Build lab_manual
cd lab_manual
## Lint the XML
xmllint --valid lab_manual/lab_manual.xml --noout
## Render the HTML
ant webhelp

# TODO Copy to directory
# cp -r data ../build_output/lab_manual

########## Shove in grc_doc
#TODO Shove in grc_doc
# mkdir ${html_dir}/grc_doc
# cp -r ${script_dir}/grc_doc/* ${html_dir}/grc_doc

########## Add static site elements
# TODO Shove in index.html and grc_doc
# cp index.html ${html_dir}