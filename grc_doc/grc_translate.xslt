<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <xsl:apply-templates select="block"/>
  </xsl:template>

  <xsl:template match="block">
    <xsl:copy>
      <xsl:apply-templates select="name"/>
      <xsl:apply-templates select="key"/>
      <doc>TODO <xsl:value-of select="./doc"/></doc>
      <xsl:apply-templates select="param"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="param">
    <xsl:copy>
      <xsl:apply-templates select="name"/>
      <doc>TODO</doc>
      <xsl:if test="not(type = 'enum')">
	<xsl:apply-templates select="type"/>
      </xsl:if>
      <xsl:if test="type = 'enum'">
	<type>
	  <xsl:apply-templates select="option"/>
	</type>
      </xsl:if>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="name">
    <xsl:copy><xsl:value-of select="."/></xsl:copy>
  </xsl:template>

  <xsl:template match="key">
    <xsl:copy><xsl:value-of select="."/></xsl:copy>
  </xsl:template>

  <xsl:template match="type">
    <xsl:copy><xsl:value-of select="."/></xsl:copy>
  </xsl:template>

  <xsl:template match="option">
    <xsl:copy>
      <xsl:apply-templates select="name"/>
      <doc>TODO</doc>
    </xsl:copy>
  </xsl:template>

</xsl:stylesheet>
