#!/bin/bash

# Nuke existing website
# rm -rf ../build_output
# mkdir ../build_output

# Build lab_manual
bash ./lab_manual/gen_html.sh

# Shove in index.html and grc_doc
cp index.html ../build_output/
cp -r grc_doc/ ../build_output/

#? Celebrate
echo "Woohoo?"
