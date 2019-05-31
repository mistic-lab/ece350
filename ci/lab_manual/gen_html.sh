#!/bin/bash


html_dir="../build_output"


# Lint the XML
xmllint --valid ../lab_manual/lab_manual.xml --noout

if [ $? != 0 ] # I xmllint threw an error, bail out with exit code 1
  then
    exit 1
fi

#TODO Doesn't exist anymore
# # Move what is currently published and make space for ant
mkdir $html_dir}/lab_manual_old
mv ${html_dir}/lab_manual/* lab_manual_old 
rm -rf ${html_dir}/lab_manual

# Render the HTML
ant webhelp

# Copy to directory
if [ $? == 0 ] # If ant did not throw an error
  then 
    cp -r ../../lab_manual/data ${html_dir}/lab_manual
    rm -rf ${html_dir}/lab_manual_old
fi

# chmod -R o+r ${html_dir}/lab_manual
