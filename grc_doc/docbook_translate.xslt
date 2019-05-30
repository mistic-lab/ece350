<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="/">
    <xsl:apply-templates select="block"/>
  </xsl:template>

  <xsl:template match="block">
    <sect2>
	<sect2info>
	<title><xsl:value-of select="name"/></title> 
	</sect2info>
	<para><xsl:value-of select="doc"/></para>
	<screenshot>
	<graphic fileref="images/{key}.png"/>
	</screenshot>
    <xsl:apply-templates select="param"/>
    </sect2>
  </xsl:template>

  <xsl:template match="param">
  <sect3>
  <sect3info>
    <title><xsl:apply-templates select="name"/></title>
    </sect3info>
    <xsl:if test="type/option">
      <para><xsl:value-of select="doc"/></para>
      <xsl:apply-templates select="type"/>
    </xsl:if>
    <xsl:if test="not(type/option)">
      <xsl:apply-templates select="type"/>
      <para><xsl:value-of select="doc"/></para>
    </xsl:if>
    </sect3>
  </xsl:template>

  <xsl:template match="type">
    <xsl:if test="option">
      <informaltable frame="none"><tgroup cols="2"><tbody>
      <xsl:for-each select="option">
      <row><entry><xsl:value-of select="name"/></entry><entry><xsl:value-of select="doc"/></entry></row>
      </xsl:for-each>
      </tbody>
      </tgroup>
      </informaltable>
    </xsl:if>	
    <xsl:if test="not(option)">
      <para><emphasis>Type: </emphasis><xsl:value-of select="."/></para>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
