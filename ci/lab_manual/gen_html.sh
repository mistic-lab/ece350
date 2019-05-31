#!/bin/bash

script_dir="$(dirname $0)"
html_dir="${script_dir}/../../build_output"

echo "#2: "
ls ${html_dir}



# Lint the XML
xmllint --valid ${script_dir}/../../lab_manual/lab_manual.xml --noout

if [ $? != 0 ] # I xmllint threw an error, bail out with exit code 1
  then
    exit 1
fi

#TODO Doesn't exist anymore
# # Move what is currently published and make space for ant
# mkdir ${html_dir}/lab_manual_old
# mv ${html_dir}/lab_manual/* ${html_dir}/lab_manual_old 
# rm -rf ${html_dir}/lab_manual
echo "#3: "
ls ${html_dir}

# Render the HTML
ant webhelp ${script_dir}/build.xml
echo "#4: "
ls ${html_dir}

# Copy to directory
if [ $? == 0 ] # If ant did not throw an error
  then 
    cp -r ${script_dir}/../../lab_manual/data ${html_dir}/lab_manual
    # rm -rf ${html_dir}/lab_manual_old
fi
echo "#5: "
ls ${html_dir}

# chmod -R o+r ${html_dir}/lab_manual
