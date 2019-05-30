<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <article>
      <articleinfo>
        <title>GNU Radio Companion</title>
	<subtitle>Block Documentation</subtitle>
	<revhistory>
	  <revision>
	    <revnumber>1.0</revnumber>
	    <date>08 Mar 2013</date>
	    <revremark>Updated for GNU Radio 3.6.3.</revremark>
	  </revision>
	</revhistory>
      </articleinfo>
      <xsl:apply-templates select="cat/cat"/>
    </article>
  </xsl:template>
    
  <xsl:template match="cat/cat">
    <sect1>
      <sect1info>
	<title><xsl:apply-templates select="name"/></title>
      </sect1info>
      <xsl:apply-templates select="block"/>
    </sect1>
  </xsl:template>

  <xsl:template match="name">
    <xsl:value-of select="."/>
  </xsl:template>

  <xsl:template match="block">
    <xsl:variable name="filename">./docbook_xml/<xsl:value-of select="."/>_doc.xml</xsl:variable>
    <xsl:copy-of select="document($filename)/*"/>
  </xsl:template>

</xsl:stylesheet>
