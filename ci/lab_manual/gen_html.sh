#!/bin/bash

script_dir="$(dirname $0)"
html_dir="${script_dir}/../../build_output"


# Lint the XML
xmllint --valid ${script_dir}/lab_manual/lab_manual.xml --noout

if [ $? != 0 ] # I xmllint threw an error, bail out with exit code 1
  then
    exit 1
fi


# Render the HTML
ant webhelp

# Copy to directory
if [ $? == 0 ] # If ant did not throw an error
  then 
    cp -r /lab_manual/data ${html_dir}/lab_manual
else
  echo "ANT COMPLAINED"
fi


