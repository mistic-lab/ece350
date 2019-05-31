#!/bin/bash

# Nuke existing website
# rm -rf ../build_output
# mkdir ../build_output

script_dir="$(dirname $0)"
html_dir=${script_dir}/../build_output

# Build lab_manual
bash ${script_dir}/lab_manual/gen_html.sh

# Shove in index.html and grc_doc
cp ${script_dir}/index.html ${html_dir}
# mkdir ${html_dir}/grc_doc
cp -r ${script_dir}/grc_doc ${html_dir}/

#? Celebrate
echo "Woohoo?"
