#!/bin/bash

script_dir="$(dirname $0)"
html_dir="${script_dir}/../../build_output"


# Lint the XML
xmllint --valid ${script_dir}/lab_manual/lab_manual.xml --noout

# Render the HTML
ant webhelp

# TODO Copy to directory
# cp -r ${script_dir}/lab_manual/data ${html_dir}/lab_manual


