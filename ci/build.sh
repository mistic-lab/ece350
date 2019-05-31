#!/bin/bash

# Nuke existing website
# rm -rf ../build_output
# mkdir ../build_output

script_dir="$(dirname $0)"
html_dir="${script_dir}/../build_output"

echo "#1: "
ls ${html_dir}

# Build lab_manual
bash ${script_dir}/lab_manual/gen_html.sh

# Shove in index.html and grc_doc
cp ${script_dir}/index.html ${html_dir}
echo "#6: "
ls ${html_dir}
# mkdir ${html_dir}/grc_doc
# cp -r ${script_dir}/grc_doc/* ${html_dir}/grc_doc

#? Celebrate
# echo "Woohoo?"
