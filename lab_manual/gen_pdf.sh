#!/bin/bash

# Packages required:
#
# xsltproc docbook-xsl-ns docbook5-xml fop
#
xsltproc -xinclude -o lab_manual.fo /usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook.xsl lab_manual.xml
fop lab_manual.fo -pdf lab_manual.pdf -d
