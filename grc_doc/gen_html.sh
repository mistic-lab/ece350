#!/bin/bash

user=`whoami`

for block in `ls doc_xml`
do
    xsltproc -o docbook_xml/$block docbook_translate.xslt doc_xml/$block
done

xsltproc -o grc_doc.xml grc_index.xslt block_tree.xml
ant webhelp

scp -r grc_doc ${user}@wireless.ece.uvic.ca:/home/elec350/.www/

