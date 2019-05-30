<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <xsl:apply-templates select="block"/>
    <br/><br/><a href="#top">Index</a><br/>
  </xsl:template>

  <xsl:template match="block">
    <hr/>
    <a name="{key}"><h2><xsl:value-of select="name"/></h2></a> 
    <img src="./images/{key}.png"/><br/><br/>
    <xsl:value-of select="doc"/>
    <xsl:apply-templates select="param"/>
  </xsl:template>

  <xsl:template match="param">
    <h3><xsl:apply-templates select="name"/></h3>
    <xsl:if test="type/option">
      <xsl:value-of select="doc"/><br/><br/>
      <xsl:apply-templates select="type"/>
    </xsl:if>
    <xsl:if test="not(type/option)">
      <xsl:apply-templates select="type"/>
      <xsl:value-of select="doc"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="type">
    <xsl:if test="option">
      <table>
      <xsl:for-each select="option">
	<tr><td><b><xsl:value-of select="name"/></b></td><td><xsl:value-of select="doc"/></td></tr>
      </xsl:for-each>
      </table>
    </xsl:if>	
    <xsl:if test="not(option)">
      <b>Type: </b><xsl:value-of select="."/><br/><br/>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
