#!/bin/bash
#########################
#
# Builds the ECE350 course website 
# Build is done by Travis CI and published to Github Pages
# 
# Date: June 2019
# Author: Nicholas Bruce
#
#########################

########### Build lab_manual
cd lab_manual
# Lint the XML
xmllint --valid lab_manual.xml --noout
# Render the HTML
ant webhelp
# Copy data for lab_manual
cp -r data ../build_output/lab_manual
cd ..

########## Shove in grc_doc
mkdir build_output/grc_doc
cp -r grc_doc/build_output/* build_output/grc_doc

########## Add static site elements
cp static_site/index.html build_output