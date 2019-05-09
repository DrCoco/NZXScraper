from bs4 import BeautifulSoup

# raw html input
#region
getStockSummaryInput = BeautifulSoup(r"""


<HTML>
<HEAD>
<TITLE>NZX Company Research - Issuer - Fundmantal Ratios & Trading Performance</TITLE>

		
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<link rel="stylesheet" href="css/styles.css?refreshcache=20150915" type="text/css">
	<link rel="shortcut icon" href="https://companyresearch-nzx-com.ezproxy.aut.ac.nz/favicon.ico?refreshcache=20150915" />
	<!-- files for highcharts -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
	<script src="https://code.highcharts.com/highcharts.js"></script>
	<script>window.jQuery || document.write('<script src="js/jquery-1.8.3.min.js"><\/script>')</script>
	<script src="https://code.highcharts.com/highcharts-more.js"></script>
	<script src="https://code.highcharts.com/modules/exporting.js"></script>
	<script src="https://highcharts.github.io/export-csv/export-csv.js"></script>
	
	<script language="JavaScript" src="FusionCharts/FusionCharts.js"></script>	<STYLE type="text/css" media="print">
	DIV {
	/*	  display: none; */
	}
	#SCROLL {
		overflow: visible;
		display: block;
	}
	</STYLE>
	<STYLE type="text/css" media="screen">
	BODY {
		overflow-y: scroll;
		margin-left: auto;
		margin-right: auto;
	}
	#SCROLL {
		vertical-align: top;
		overflow-x: auto;
		overflow-y: auto;
		border: 0px solid #00397D;
	}
	</STYLE>  
	<STYLE type="text/css" media="print">
	TD.SCROLLCELL {
		overflow: visible;
		display: block;
	}
	</STYLE>
	<STYLE type="text/css" media="screen">
	TD.SCROLLCELL {
		vertical-align: top;
		overflow-x: auto;
		overflow-y: auto;
		border: 0px solid #00397D;
	}
	</STYLE>
	<STYLE type="text/css">
	table.body {
		width:960px;
		display: block;
	}
	</STYLE>

	<link type="text/css" media="print" rel="stylesheet" href="css/print.css">
	<link type="text/css" media="screen" rel="stylesheet" href="css/superfish-da.css">
	<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
	<script type="text/javascript" src="js/hoverIntent.js"></script>
	<script type="text/javascript" src="js/superfish.js"></script>
	<script type="text/javascript" src="js/jquery.autocomplete.min.js"></script>
	<script type="text/javascript" src="js/da_search.js"></script>
	<script type="text/javascript">jQuery(function(){ jQuery('ul.sf-menu').superfish(); });</script>
	<link type="text/css" rel="stylesheet" href="js/jquery.autocomplete.css?refreshcache=20131023" />
	
	<!--[if IE 6]>
	<link href="css/ie6.css" media="screen" rel="stylesheet" type="text/css" />
	<![endif]-->
	<!--[if IE 7]>
	<link href="css/ie7.css" media="screen" rel="stylesheet" type="text/css" />
	<![endif]-->
	<!--[if IE 8]>
	<link href="css/ie8.css" media="screen" rel="stylesheet" type="text/css" />
	<![endif]-->
	<!--[if IE 9]>
	<link href="css/ie9.css" media="screen" rel="stylesheet" type="text/css" />
	<![endif]-->

<script type="text/javascript" src="//script.crazyegg.com/pages/scripts/0083/6525.js" async="async"></script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-38011745-1', 'auto');
  ga('set', '&uid', {112});
  ga('send', 'pageview');

</script>

	<script type="text/javascript">
	
	  var _gaq = _gaq || [];
	  _gaq.push(['_setAccount', 'UA-38011745-2']);
	  _gaq.push(['_setDomainName', 'nzx.com']);
	  _gaq.push(['_trackPageview']);
	
	  (function() {
		 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
	  })();
	
	</script>

	<script type="text/javascript">
	var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
	document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
	</script>
	<script type="text/javascript">
	try {
	var pageTracker = _gat._getTracker("UA-7183078-1");
	pageTracker._setCustomVar(1, "ID", "112", 3)
	pageTracker._setCustomVar(2, "Service", "Company Research", 3)
	pageTracker._trackPageview();
	} catch(err) {}</script>

</HEAD>

<BODY height="*" width="960" style="background-image:url('pages/images/nzx_bg.gif'); background-repeat:repeat">
	<A NAME="top"></A>
	<div id="content" height="*">
<CENTER>

	<TABLE HEIGHT="*" WIDTH="960" PADDING="0" MARGIN="0" CELLSPACING="0" CELLPADDING="0">
	
		<TR class="logoarea" height="80">
			<TD WIDTH="960">
			
				<!-- LOGO AREA -->
				<TABLE HEIGHT="*" WIDTH="960" PADDING="0" MARGIN="0" CELLSPACING="0" CELLPADDING="0">
					<TR>
						<TD width="565">
							<!-- padding around new logo should be half the height of the logo. make the table 2x the height of the logo -->
							<img style="height:40px; padding:10px 20px 10px 0px;" align="top" src="../global/images/NZX_REVERSE_web.png" alt="NZX Limited">
							<span class="logoarea" style="vertical-align:-30px; font-size:28px; opacity:1; color:#0060A1;"  nowrap>Company&nbsp;Research</span>
						</TD>
						<TD width="395">
							<div class="noprint">
		
	<!--
			<span style="color:#FFFFFF;font-size:11px; font-weight:normal; margin-left:11px; line-height:10px">Enter at least the first 3 characters of the issuer's name or code,<BR></span>
			<span style="color:#FFFFFF;font-size:11px; font-weight:normal; margin-left:11px">then make your selection in the results box below.</span>
	-->
			<div id="da_search_box" style="text-align:left; padding: 0px 0px 0px 4px; height:28px; border:solid 0px red; font-family:verdana;">
				<form style="border:0; background-color:transparent;" id="da_search_form" name="da_search" action="da_search.php" method="POST">
				<input type="hidden" name="q_id" id="search_query_id" value="" />
				<input type="submit" id="searchGo" value="" style="float:right; vertical-align:top; background:url('images/search-icon.png'); background-repeat:no-repeat; width:32px; height:28px; border:0px;" />  
				<input type="text" name="q" id="search_query" value="" class="ac_input" style="float:right; width:300px; height:28px; font-size:14px; align:right;
				border:solid 1px #e0e0e0; background: #ffffff; border-radius: 0px 0px 0px 0px; -moz-appearance: textfield;" autocomplete="off" placeholder="Search for an index, sector, or issuer." />
	
	
				<!-- <input type="submit" id="searchGo" value="Search" style="margin-left:5px;"/> -->  
				<!-- <input type="image" src="images/search-icon.png" border="0" alt="Submit" />  -->
	
				</form>	
			</div>
										</div>
						</TD>
					</TR>
				</TABLE>
				<!-- END LOGO AREA -->
				
			</TD>
		</TR>
		
		
		<TR class="noprint" height="30" width="100%">
			<TD WIDTH="960" style="background-color:#0061A2;">
			
				<!-- MENU AREA -->
				<ul class="sf-menu" width="960" style="width:960;">
	
	<li><a href="index.php">Home</a></li>
	
	<li><a href="index.php?pageid=about">About</a></li>

	
	
	<li><a href="">Trading Data</a>
		<ul style="width:200px">
			<li><a href="index.php">Market Overview</a></li>
			<li><a href="index.php?pageid=livenews">Market Announcements</a></li>
			<li><a href="index.php?pageid=liveindex">Indices &#38; Sectors Activity</a></li>

			<li><a href="index.php?pageid=live_market">Market Activity / Share Prices</a></li>
<!--		<li><a href="index.php?pageid=live_market&#38;CODE=NZSX">NZSX Market Activity</a></li>
			<li><a href="index.php?pageid=live_market&#38;CODE=NXT">NXT Market Activity</a></li>
			<li><a href="index.php?pageid=live_market&#38;CODE=FSM">FSM Market Activity</a></li>
			<li><a href="index.php?pageid=live_market&#38;CODE=NZAX">NZAX Market Activity</a></li>
			<li><a href="index.php?pageid=live_market&#38;CODE=NZDX">NZDX Market Activity</a></li>
			<li><a href="index.php?pageid=live_market&#38;CODE=DFUT">Dairy Derivatives Market Activity</a></li>
			<li><a href="index.php?pageid=live_market&#38;CODE=EFUT">Equity Derivatives Market Activity</a></li>
	-->		
			<li><a href="index.php?pageid=live_ratios">Market Ratios</a></li>

			<li><a href="market_summary.php">Historic Trading Activity</a></li>
			<li><a href="trading_summary.php">Market Summary Charts</a></li>
			<li><a href="trading_summary.php?drilldown=1">Top Traded Securities Chart</a></li>
		</ul>
	</li>
	<!--<span style="color:red">(new)</span>-->
	<li><a href="">Searches &amp; Tools</a>
		<ul style="width:180px">
			<li><a href="search_prices.php">Adjusted Share Prices Tool</a></li>
			<li><a href="search_announcements_form.php">Announcements Search Tool</a></li>
			<li><a href="index.php?pageid=divhistory">Dividend History Tool</a></li>
			<li><a href="search_profiles_form.php">Profile Search Tool</a></li>
			<li><a href="market_summary.php">Historic Trading Activity</a></li>
		</ul>
	</li>
	
	<li><a href="">Professionals</a>
		<ul style="width:160px">
			<li><a href="index.php?pageid=auditfees">Auditors Fees</a></li>
			<li><a href="index.php?pageid=divcalendar">Upcoming Dividends</a></li>
			<li><a href="market_summary.php">Historic Trading Activity</a></li>
			<li><a href="trading_summary.php">Market Summary Charts</a></li>
		</ul>
	</li>
	
	<li><a href="">Events</a>
		<ul style="width:180px">
			<li><a href="index.php?pageid=codes&#38;code=LL">Current Listed Issuers</a></li>
			<li><a href="index.php?pageid=codes&#38;code=A">Adjustments / Capital Events</a></li>
			<li><a href="index.php?pageid=codes&#38;code=L">Issuer Listing Dates</a></li>
			<li><a href="index.php?pageid=codes&#38;code=SL">Security Listing Dates</a></li>
			<li><a href="index.php?pageid=codes&#38;code=R">Issuer Name Changes</a></li>
			<li><a href="index.php?pageid=codes&#38;code=SR">Security Name Changes</a></li>
			<li><a href="index.php?pageid=codes&#38;code=D">Issuer Delisting Dates</a></li>
			<li><a href="index.php?pageid=codes&#38;code=SD">Security Delisting Dates</a></li>
			<li><a href="index.php?pageid=divcalendar">Upcoming Dividends</a></li>
<!--		
			<li><a href="index.php?pageid=search_codes">What happened to an issuer?</a></li>
			 <span style="color:red">(new)</span>
-->
		</ul>
	</li>
	
<!--
	<li>
		<a href="">Searches</a>
		<ul style="width:200px">
			<li><a href="search/major_search.php?new=1">Major Shareholders</a></li>
			<li><a href="search/nzcsd_search.php">NZCSD Holders</a></li>
			<li><a href="search_codes.php">What happened to an issuer?</a></li>
			<li><a href="query_builder.php">Financials</a></li>
			<li><a href="search/directory_search.php">Directory</a></li>
		</ul>
	</li>
-->
	

	<li><a href="">Indices &amp; Sectors</a>
		<ul style="width:200px">
		
			<li><a href="index.php?pageid=indices_methodology"><nobr>Indices Transition &amp; Methodology</nobr></a></li>
			<li><a href="index.php?pageid=sectors_methodology"><nobr>Sectoral Indices Transition</nobr></a></li>
			
			<li><a href=""><nobr>Equity Indices</nobr></a>
				<ul style="width:230px">
					<li><a href="index.php?pageid=sector_overview&#38;CODE=AXAS">S&amp;P/NZAX All Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=ALL">S&amp;P/NZX All Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=T10">S&amp;P/NZX 10 Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=NZ20">S&amp;P/NZX 20 Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=NZ50">S&amp;P/NZX 50 Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=HDI">S&amp;P/NZX 50 High Dividend Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=NC50">S&amp;P/NZX 50 Portfolio Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=SEMC">S&amp;P/NZX MidCap Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=SCI">S&amp;P/NZX SmallCap Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=FWPP">S&amp;P/NZX Primary Sector Equity</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=FWPI">S&amp;P/NZX Primary Sector Investable Equity</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=NZRS">S&amp;P/NZX Real Estate Select</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=MOR">S&amp;P/NZX Morrison Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=T40">NZSE 40 Index (historic)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=BCLY">Barclays Index (historic)</a></li>
				</ul>
			</li>
<!--			
			<li><a href=""><nobr>Agriculture Indices <span style="color:red">(new)</span></nobr></a>
				<ul style="width:360px">
					<li><a href="index.php?pageid=sector_overview&#38;CODE=FWA">S&amp;P/NZX Farmers Weekly Agriculture Equity Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=FWAI">S&amp;P/NZX Farmers Weekly Agriculture Investable Equity Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=FWPI">S&amp;P/NZX Farmers Weekly Primary Sector Investable Equity Index</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=FWPP">S&amp;P/NZX Farmers Weekly Primary Sector Equity Index</a></li>
				</ul>
			</li>
-->
			<li><a href=""><nobr>S&amp;P/NZX Sector Indices</nobr></a>
				<ul style="width:300px">
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G25">S&amp;P/NZX All Consumer Discretionary (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G30">S&amp;P/NZX All Consumer Staples (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G10">S&amp;P/NZX All Energy (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G40">S&amp;P/NZX All Financials (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G35">S&amp;P/NZX All Health Care (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G20">S&amp;P/NZX All Industrials (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G45">S&amp;P/NZX All Information Technology (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G15">S&amp;P/NZX All Materials (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G60">S&amp;P/NZX All Real Estate (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G50">S&amp;P/NZX All Communication Services (Sector)</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G55">S&amp;P/NZX All Utilities (Sector)</a></li>
				</ul>
			</li>
	
<!--
			<li><a href="index.php?pageid=sectorsNZ"><nobr>Sector Constituents</nobr></a></li>
-->
			
<!--
			<li><a href="index.php?pageid=sectorsNZStats&#38;chart=S"><nobr>Market Average Ratios</nobr></a></li>
-->
			
			<li><a href=""><nobr>Historic NZX Sectors</nobr></a>
				<ul style="width:210px">
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G01">PRIMARY</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A01">Agriculture &#38; Fishing</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A02">Mining</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A03">Forestry &#38; Forest Products</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A04">Building Materials &#38; Construction</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G02">ENERGY</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G03">GOODS</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A06">Food &#38; Beverages</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A07">Textiles &#38; Apparel</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A08">Intermediate &#38; Durables</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G04">PROPERTY</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G05">SERVICES</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A10">Transport</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A11">Ports</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A12">Leisure &#38; Tourism</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A13">Consumer</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A14">Media &#38; Telecommunications</a></li>
					<li style="text-indent:8px"><a href="index.php?pageid=sector_overview&#38;CODE=A15">Finance &#38; Other Services</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G06">INVESTMENT</a></li>
				</ul>
			</li>

			<!--
			<li><a href=""><nobr>GICS Sectors<span style="color:red">(new)</span></nobr></a>
				<ul style="width:210px">
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G10">SindicesP/NZX All Energy</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G15">S&amp;P/NZX All Materials</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G20">S&amp;P/NZX All Industrials</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G25">S&amp;P/NZX All Consumer Discretionary</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G30">S&amp;P/NZX All Consumer Staples</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G35">S&amp;P/NZX All Health Care</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G40">S&amp;P/NZX All Financials</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G45">S&amp;P/NZX All Information Technology</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G50">S&amp;P/NZX All Telecommunication Services</a></li>
					<li><a href="index.php?pageid=sector_overview&#38;CODE=G55">S&amp;P/NZX All Utilities</a></li>
				</ul>
			</li>
			-->
				
		</ul>
	</li>
	
<!--
	<li><a style="color:#505050;" href="../crust/services.php">Services</a></li>
	<li><a style="color:#505050;" href="../crust/logout.php">Logout</a></li>
-->

	<!-- note element is floated right, so is moved to last item on menu -->
	<li style="float:right;"><a href="">Login Options</a>
		<ul style="width:130px">
			<li><a href="../crust/profile.php?act=chemail">Change Email</a></li>
			<li><a href="../crust/profile.php?act=chpasswd">Change Password</a></li>
			<li><a href="../crust/services.php">Services List</a></li>
			<li><a href="../crust/logout.php">Log out</a></li>
		</ul>
	</li>
	<!-- note element is floated right, so is moved to 2nd-to-last item on menu -->
	<li style="float:right;"><!-- class="grey" --><a href="index.php?pageid=conditions">Conditions of Use</a></li>

</ul>
				<!-- END MENU AREA -->
				
			</TD>
		</TR>
		
		
		<!-- MAINTENANCE BANNER -->
	<!--	
		<TR>
			<TD colspan="3" style="padding:10px; font-weight:normal; border:solid 5px white; background:#F9DE0E; line-height:150%;">
				<p color=#FF0000 style="font-size:12px; line-height:120%;">
				Due to maintenance there will be periods between 10.30am - 3.30pm on Saturday 9th of June where this website is temporarily unavailable.
				<p color=#FF0000 style="font-size:12px; line-height:120%;">
                If you have any queries regarding this please <a class="text" href="mailto:data@nzx.com?subject=Company Research Maintenance">email our Research Team</a>, or phone on +64 4 471 4390.
			</TD>
		</TR>
       -->
		<!-- END MAINTENANCE BANNER -->
		
		
		<TR HEIGHT="*" VALIGN="TOP">
			<TD WIDTH="960" style="padding-top:10px;" VALIGN="TOP">
			
	
				<!--PLACE WHOLE PAGE WITHIN A TABLE-->
				<TABLE CLASS="body" CELLSPACING="0" CELLPADDING="0" HEIGHT="*" WIDTH="960" MARGIN="0" style="max-width:960px; width:960px;">
					<TR HEIGHT="*" VALIGN="TOP">
						<TD WIDTH="960" style="padding-top:10px;" VALIGN="TOP">
						<!-- START LEVEL 1-->
			
								
				
				<!-- insert custom message for AUT users -->
								<!-- end custom message -->
				
				
				<!-- START PAGE -->


<TR style="height:100%;border:solid 1px"><TD class="leftmenu" valign="top" height="100%" style="padding:0px; width:80px"><table class="innermenu" width="120" style="height:100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="heading">&raquo;	Company Info</td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=overview&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=overview&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Overview</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=dir&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=dir&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Company Directory</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=prof&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=prof&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Company Profile</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=kom&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=kom&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Key Milestones</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=bondprof&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=bondprof&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Bond Profiles</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=news&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=news&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Market Announcements</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=arep&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=arep&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Annual Reports</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=event&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=event&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Events & Documents</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=divs&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=divs&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Dividend & Interest Payments</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=fcst&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=fcst&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Brokers Forecasts</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=finpro&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=finpro&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Financial Profile</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=secs&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=secs&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Listed Securities</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=tearsheet&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=tearsheet&amp;default=TLS'" nowrap><span style="white-space: nowrap;">Tear Sheet</span></td></tr><tr><td class="heading">&raquo;	Security Info</td></tr><tr><td class="menuon" style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;
	color:#0060A1; font-weight:bold; padding-left:5px;" nowrap><span style="white-space: nowrap;"><big>&raquo;</big>&nbsp;Summary & Ratios</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=orderbook&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=orderbook&amp;default=TLS'" nowrap><span style="white-space: nowrap">Live Orderbook</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=price&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=price&amp;default=TLS'" nowrap><span style="white-space: nowrap">Historical Prices</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=chart&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=chart&amp;default=TLS'" nowrap><span style="white-space: nowrap">Historical Price Chart</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=ratios_history_chart&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=ratios_history_chart&amp;default=TLS'" nowrap><span style="white-space: nowrap">Historical Ratios Chart</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=candle&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=candle&amp;default=TLS'" nowrap><span style="white-space: nowrap">Candlestick Chart</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=topsh&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=topsh&amp;default=TLS'" nowrap><span style="white-space: nowrap">Top Shareholders</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=nzcsd&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=nzcsd&amp;default=TLS'" nowrap><span style="white-space: nowrap">NZCSD Holders</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=shares&amp;default=TLS" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=shares&amp;default=TLS'" nowrap><span style="white-space: nowrap">Share Transactions</span></td></tr><tr><td class="heading">&raquo;	Listed Securities</td></tr><tr><td class="menuon" style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;
	color:#0060A1; font-weight:bold; padding-left:5px;" nowrap><span style="white-space: nowrap;"><big>&raquo;</big>&nbsp;<B>TLS</B>, Telstra Corporation Limited Ordinary Shares</span></td></tr><tr><td class="heading">&raquo;	Delisted Securities</td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=livedata&amp;default=TLSCA" title="Telstra Corporation Installment Receipts" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=livedata&amp;default=TLSCA'" nowrap><span style="white-space: nowrap"><B>TLSCA</B>, Telstra Corporation Installment Receipts</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=livedata&amp;default=TLSCB" title="Telstra Corporation Instalment Receipts" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=livedata&amp;default=TLSCB'" nowrap><span style="white-space: nowrap"><B>TLSCB</B>, Telstra Corporation Instalment Receipts</span></td></tr><tr class="" onclick="top.location.href=newpage.php?pageid=livedata&amp;default=TLSCC" title="Telstra Corporation Limited Instalment Receipts" onmouseover="javascript:this.className='HoverMe'" onmouseout="this.className=''"><td style="max-width:160px; width:160px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;"class="menuoff" onclick="top.location.href='newpage.php?pageid=livedata&amp;default=TLSCC'" nowrap><span style="white-space: nowrap"><B>TLSCC</B>, Telstra Corporation Limited Instalment Receipts</span></td></tr><tr style="height:100%"><td height="100%" style="padding-bottom:20px;border-bottom:0px; empty-cells: show"></td></tr></table></TD>
	<TD valign="top" width="100%" height="100%" style="padding:0px; padding-left:8px;">
		<!--DIV style="overflow-y: scroll"-->
			<TABLE style="height:100%" cellspacing="0" cellpadding="0" width="100%">
				<TR>
					<TD VALIGN="TOP" BGCOLOR="#FFFFFF">
				<h1>Telstra Corporation Limited - TLS (Telstra Corporation Limited Ordinary Shares)
				</h1><font class="heading">Summary & Ratios<p><font style="font-weight:normal; color:#000000;"><span class="greytext">Prices quoted in $ per security
<table class="section" cellspacing="0" cellpadding="0">
	<tr class="heading">
		<td>Listing Details</td>
		<td style="padding-left:10px;">Fundamental Ratios</td>
	</tr>
	<tr>
	
		<td valign="top">

			<table class="data" cellspacing="0" cellpadding="0">
				
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">
					<td class="dir_left">Description</td>
					<td colspan=3>Telstra Corporation Limited Ordinary Shares</td>
				</tr>
				
				<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">
					<td class="dir_left">Ticker</td>
					<td>TLS</td>
					<td class="dir_left">ISIN</td>
					<td>AU000000TLS2</td>
				</tr>
				
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">
					<td class="dir_left"><nobr>Listing Status</nobr></td>
					<td class="dir_right">Active
					</td>
					
					<td class="dir_left">Quote Basis</td>
					<td>$ per security
					</td>
				</tr>
				
				<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">
					<td class="dir_left">Market</td>
					<td>NZSX
					</td>
					<td class="dir_left">Coupon Rate</td>
					<td class="dir_right">-</td>
				</tr>
				
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">
					<td class="dir_left">Registry</td>
					<td class="dir_right"><a title="view registry details" href="newpage.php?pageid=registry&default=TLS">LNKT</a></td>
					<td class="dir_left"><nobr>Coupon Frequency</nobr></td>
					<td class="dir_right">-</td>
				</tr>
				
				<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">
					<td class="dir_left">Listed Date</td>
					<td class="dir_right"><nobr>2 Nov 1998</nobr></td>
					<td class="dir_left">Next Record Date</td>
					<td class="dir_right"><nobr>-
						</nobr>
					</td>
				</tr>
				
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">

					<td class="dir_left"><nobr>Delisted Date</nobr></td>
					<td class="dir_right"><nobr>-
					</td>

					<td class="dir_left">Maturity Date</td>
					<td class="dir_right">-
					</td>
				</tr>
			</table>	

		</td>
		<td valign="top" style="padding-left:10px;">

			<table class="data" cellspacing="0" cellpadding="0">
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">	<td width=40 class="dir_left" style="white-space:nowrap;"><NOBR>Price Change</td>
			<td class="dir_right" align="center"><B><big></big><span class="greytext"><i>no change</i></span></big></B></td>
			<td class="dir_left" align="left"><NOBR>Market Price</td>
			<td class="dir_right" align="center"><B><big><span style="padding-right:2px">$</span>3.63</big></B></td></tr><tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">	<td class="dir_left" style="white-space:nowrap;"><NOBR>No. on issue</td><td class="dir_right" align="right">11,893,297,855</span></td>	<td  class="dir_left" style="white-space:nowrap;"><NOBR>Marketcap</td><td class="dir_right" align="right"><span style="padding-right:2px">$</span>43,172,671,214</td>
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">
					<td class="dir_left" width=40 style="white-space:nowrap;"><NOBR>EPS</td>
					<td class="dir_right" width=40 align="right"><span color=black><span style="padding-right:2px">$</span>0.272905</span></td>
					<td class="dir_left" width=40 style="white-space:nowrap;"><NOBR>P/E ratio</td>
					<td class="dir_right" width=40 align="right">13.301332</td>
				</tr>
				<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">
					<td class="dir_left" style="white-space:nowrap;"><NOBR>NTA</td>
					<td class="dir_right" align="right"><span color=black><span style="padding-right:2px">$</span>0.591760</span></td>
					<td class="dir_left" style="white-space:nowrap;"><NOBR>Price/NTA</td>
					<td class="dir_right" align="right"><span color=black>6.134244</span></td>
				</tr>
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">
					<td class="dir_left" style="white-space:nowrap;"><NOBR>Net DPS</td>
					<td class="dir_right" align="right"><span style="padding-right:2px">$</span>0.203150</td>
					<td class="dir_left" style="white-space:nowrap;"><NOBR>Net Yield</td>
					<td class="dir_right" align="right">5.596419</td>
				</tr>
				<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">
					<td class="dir_left" style="white-space:nowrap;"><NOBR>Gross DPS</td>
					<td class="dir_right" align="right"><span style="padding-right:2px">$</span>0.203150</td>
					<td class="dir_left" style="white-space:nowrap;"><NOBR>Gross Yield</td>
					<td class="dir_right" align="right">5.596419</td>
				</tr>
				<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">
					<td class="dir_left" style="white-space:nowrap;"><NOBR>Beta Value</td>
					<td class="dir_right" align="right"><span color=black>0.280854</span></td>
					<td class="dir_left" style="white-space:nowrap;"><NOBR>Sharpe Ratio</td>
					<td class="dir_right" align="right"><span color=black>0.497835</span></td>
				</tr>

			</table>
			
		</td>
	</tr>
</table>
<table class="section" cellspacing="0" cellpadding="0">
	<tr class="heading">
		<td>Trading Performance</td>
	</tr>
</table><table class="data" width="100%" cellspacing="0" cellpadding="0">	<tr class="heading">		<td align="right" style="empty-cells:show"></td>		<td align="right" title="hint: price before trading began">Open</td>		<td align="right" title="hint: gross return (calculated on basis that dividends are reinvested)">% Return</td>		<td align="right" title="hint: closest active Buy quote (to buy shares)">Bid</td>		<td align="right" title="hint: closest active Sell quote (to sell shares)">Ask</td>		<td align="right" title="hint: highest sale price achieved">High</td>		<td align="right" title="hint: lowest sale price achieved">Low</td>		<td align="right" title="hint: number of shares traded">Volume Traded</td>		<td align="right" title="hint: dollar value of shares traded">$ Value Traded</td>		<td align="right" title="hint: volume weighted average price">VWAP</td>		<td align="right" title="hint: number of share transactions">Trades</td>	<tr>	<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">		<td class="dir_left">Today</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>3.630</td>		<td class="dir_right" align="right" style="white-space:nowrap;">-		</td>		<td class="dir_right" align="right"><span style="padding-right:2px">$</span>3.550</td>		<td class="dir_right" align="right"><span style="padding-right:2px">$</span>3.620</td>		<td class="dir_right" align="right">-</td>		<td class="dir_right" align="right">-</td>		<td class="dir_right" align="right">-</td>		<td class="dir_right" align="right">-</td>		<td class="dir_right" align="right">-</td>		<td class="dir_right" align="right">-</td>	</tr>	<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">		<td class="dir_left">This Week</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>3.630</td>		<td class="dir_right" align="right" >-</td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="right" >-</td>		<td class="dir_right" align="right" >-</td>		<td class="dir_right" align="right" >-</td>		<td class="dir_right" align="right" >-</td>		<td class="dir_right" align="right" >-</td>		<td class="dir_right" align="right" >-</td>	</tr>	<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">		<td class="dir_left">This Month</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>3.450</td>		<td class="dir_right" align="right" ><span class="greentext"><SPAN STYLE="PADDING-RIGHT:2PX">+</SPAN>5.22<span style="padding-left:1px">%</span></span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>3.630</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>3.420</td>		<td class="dir_right" align="right" >182,007</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>636,504.64</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>3.4971</td>		<td class="dir_right" align="right" >276</td>	</tr>	<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">		<td class="dir_left">This Year</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>2.867</td>		<td class="dir_right" align="right" ><span class="greentext"><SPAN STYLE="PADDING-RIGHT:2PX">+</SPAN>26.62<span style="padding-left:1px">%</span></span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>3.630</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>2.867</td>		<td class="dir_right" align="right" >887,660</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>2,940,444.02</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>3.3126</td>		<td class="dir_right" align="right" >962</td>	</tr>	<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">		<td class="dir_left">Rolling Year</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>3.078</td>		<td class="dir_right" align="right" ><span class="greentext"><SPAN STYLE="PADDING-RIGHT:2PX">+</SPAN>17.93<span style="padding-left:1px">%</span></span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>3.630</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>2.664</td>		<td class="dir_right" align="right" >5,219,501</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>16,635,749.72</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>3.1872</td>		<td class="dir_right" align="right" >3,795</td>	</tr>	<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">		<td class="dir_left">3 Years</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>4.949</td>		<td class="dir_right" align="right" ><span class="redtext"><SPAN STYLE="PADDING-RIGHT:3PX">-</SPAN>26.65<span style="padding-left:1px">%</span></span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>5.138</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>2.664</td>		<td class="dir_right" align="right" >46,871,503</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>219,471,771.11</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>4.6824</td>		<td class="dir_right" align="right" >8,005</td>	</tr>	<tr class="dataOff" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOff'">		<td class="dir_left">5 Years</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>4.110</td>		<td class="dir_right" align="right" ><span class="redtext"><SPAN STYLE="PADDING-RIGHT:3PX">-</SPAN>11.68<span style="padding-left:1px">%</span></span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>5.718</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>2.664</td>		<td class="dir_right" align="right" >98,091,951</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>526,998,335.51</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>5.3725</td>		<td class="dir_right" align="right" >10,434</td>	</tr>	<tr class="dataOn" onmouseover="javascript:this.className='HoverMe'" onmouseout="javascript:this.className='dataOn'">		<td class="dir_left">10 Years</td>		<td class="dir_right" align="center"><span style="padding-right:2px">$</span>2.074</td>		<td class="dir_right" align="right" ><span class="greentext"><SPAN STYLE="PADDING-RIGHT:2PX">+</SPAN>75.03<span style="padding-left:1px">%</span></span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="center"><span class="greytext">n/a</span></td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>5.718</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>1.857</td>		<td class="dir_right" align="right" >930,072,901</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>4,104,959,090.46</td>		<td class="dir_right" align="right" ><span style="padding-right:2px">$</span>4.4136</td>		<td class="dir_right" align="right" >21,658</td>	</tr></table><p><font style="font-weight:normal; color:#000000; font-size:12px;"><i>Prices and Returns displayed in Trading Performance are adjusted for capital events & dividend payments (excludes Volume Traded, $ Value Traded, VWAP, and Trades)</i>
					</TD>
				</TR>
			</TABLE>
		<!--/DIV-->
	</TD>
</TR>

<!--/TABLE-->
<!--/DIV-->
						</TD>
					</TR>
				</TABLE>
<BR>				
			<!-- FOOTER AREA -->
			</TD>
		</TR>
	
		<TR HEIGHT="50">
			<TD WIDTH="100%">
	
				<TABLE HEIGHT="100%" width="960" cellspacing="0" cellpadding="0">
					<TR HEIGHT="100%">
						<TD style="width:100%; border-top:solid 7px #0061a2;">
							<a href="/" style="float:left; text-align:left; margin-left:00px; margin-top:5px;"><img alt="NZX" height="20" border="0" src="https://companyresearch-nzx-com.ezproxy.aut.ac.nz/global/images/NZX_REVERSE_web.png" width="70" /></a>
							<span style="float:left; text-align:left; margin-left:00px; margin-top:7px;">&nbsp;&nbsp;&copy; Copyright 2019 NZX Limited.</span>
							<a class="text" style="float:right; text-align:right; margin-left:20px; margin-top:5px;" href="http://www.nzxgroup.com" target="_blank">Corporate Information</a>
							<a class="text" style="float:right; text-align:right; margin-left:20px; margin-top:5px;" href="index.php?pageid=about">Contact Us</a>
							<a class="text" style="float:right; text-align:right; margin-left:20px; margin-top:5px;" href="index.php?pageid=conditions">Conditions of Use</a>
						</TD>
					</TR>
				</TABLE>
				
			</TD>
		</TR>
		
	</TABLE>
</CENTER>
	<!-- END FOOTER -->""", 'lxml')
	#endregion

