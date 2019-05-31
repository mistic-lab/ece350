#!/bin/bash

script_dir="$(dirname $0)"
html_dir="${script_dir}/../build_output"


# Build lab_manual
cd lab_manual
bash gen_html.sh

# Shove in index.html and grc_doc
cd ..
cp index.html ${html_dir}

#TODO Shove in grc_doc
# mkdir ${html_dir}/grc_doc
# cp -r ${script_dir}/grc_doc/* ${html_dir}/grc_doc

