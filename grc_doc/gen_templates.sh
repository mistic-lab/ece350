#!/bin/bash

GRC_XML_PATH="/usr/local/share/gnuradio/grc/blocks"

for blk in `cat BLOCKS`
do
    xsltproc grc_translate.xslt ${GRC_XML_PATH}/${blk}.xml > ./doc_xml/${blk}_doc.xml
done
