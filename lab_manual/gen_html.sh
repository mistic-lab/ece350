#!/bin/bash

REPOS="$1"
REV="$2"
html_dir="/home/ece350/public_html"

# Update this workspace from the repository
svn update

# Put a "Building" Message
mv ${html_dir}/lab_manual ${html_dir}/lab_manual_old
mkdir ${html_dir}/lab_manual
echo "<html><head><title>Building content from $REPOS revision $REV.</title></head><body>See <a href="../build.txt">Build Output</a> for details.</body></html>" > ${html_dir}/lab_manual/index.html
rm -rf ${html_dir}/lab_manual_old

# Lint the XML
xmllint --valid lab_manual.xml --noout

if [ $? != 0 ] 
  then
    exit 1
fi

# Render the HTML
ant webhelp

# Copy to directory
if [ $? == 0 ] 
  then 
    rm -rf ${html_dir}/lab_manual
    mv lab_manual/lab_manual/* lab_manual
    rm -rf lab_manual/lab_manual
    mv lab_manual ${html_dir}
    cp -r data ${html_dir}/lab_manual
fi

chmod -R o+r ${html_dir}/lab_manual
