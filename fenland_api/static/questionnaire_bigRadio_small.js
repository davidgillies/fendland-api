
<style type="text/css">

html {
	font-family:Verdana, Geneva, sans-serif;
	font-size:0.4em;
	text-align:justify;
	margin:0;
	padding:0;
}

body {
	margin:0;
	padding:0;
}

input {
	margin:0;
	padding:0;
	border:0;
}

table tr td {
	font-family:Verdana, Geneva, sans-serif;
	/*font-size:1.0em;*/
	font-size:0.5em;
}

#homeBanner {
	height:auto;
	width:auto;
	background-color:#422e5d;
}


/* for the homebanner image to scale when resizing the window */
#homeBanner  img {
	max-width:100%; 
	width:auto;
	height:auto;
	margin:auto;
	display:block;
}

#barcode_image{
	height: auto;
	width:auto; 
	max-width:100px; 
	max-height:100px;
}

/* meter */

meter {
	width:50%;
}

#page_meter {
	text-align:center;
}

/*To scale the images in the page*/

img.home_logos {
  width:15%;
  height:auto;
}

img.logos {
  width:15%;
  height:auto;
}

img.section_image {
  width:90%;
  height:auto;
}

/*it doesn't work*/
img.option_image{
	width:10%;
  	height:auto;
}

#logos{
	padding:0;
}

#participant{
	position: relative;
	left:35%;
	text-align: center;
	font-style:italic;
	font-size:1em;
	font-weight:normal;
	color:blue;
}

/* Page structuring */

.questionnaire_list{
	margin: 0px auto 0px auto;
	width: 50%;
	height:45%;
	overflow:auto;
}


#page_container {
   	position:relative;
   	width:100%;
}

.home_page_structurer {
	font-family:Verdana, Geneva, sans-serif;
	margin:0;
}

.page_structurer {
	font-family:Verdana, Geneva, sans-serif;
	margin:10px;
	margin-bottom:0px;
}

#page_header {
	/*font-size:1.2em;*/
	font-size:0.8em;
	text-align:center;
	font-weight:bold;
	background-color:#422e5d;
	color:white;
}

#page_body {
	/*font-size:1.2em;*/
	font-size:0.6em;
	text-align:center;
}

#questionnaire_title {
	/*font-size:1.8em;*/
	font-size:0.9em;
	font-weight:bold;
	background-color:red;
	/*background-color:#183569;*/
	color:#FFFFFF;
	text-align:center;
	padding:10px;
	border:3px ridge #637595;
}

#questionnaire_subtitle {
	/*font-size:3.0em;*/
	font-size:1.5em;
	text-align:center;
}

#questionnaire_header {
	/*font-size:1.8em;*/
	font-size:0.9em;
	text-align:center;
}

#questionnaire_text_body {
	/*font-size:1.6em;*/
	font-size:0.8em;
}

#questionnaire_footer {
	/*font-size:1.4em;*/
	font-size:0.7em;
	font-style:italic;
	text-align:center;
}

#page_content {
	padding:0px;
	margin-top:2px;
}


#page_footer {
	clear:both;
	height:25px;
	margin-top:0px;  
}

 
#page_menu  ul li a:link, #page_menu ul li a:visited {
	font-weight:bold;
	color:#FFFFFF;
	background-color:#808080;
	text-align:center;
	padding:6px;
	text-decoration:none;
}

#page_menu ul li a:hover,a:active {
	background-color:#872b8c;
}


.col-left {
	float:left;
}

.col-right {
	float:right;
}


#footer, #footer div, #footer a{
	color:black;
}



/* To force it to open on a new window rather than a new tab in the same browser. It is used mainly for Chrome as it is opening the new window in a new tab */
.popup{
	target-new:window;
}

#home_hr{
	margin:0;
	padding:0;
}

.home_link_div{
	text-align:right;
	margin:0;
	padding:5px;
	background-color:#422e5d;
}

.link_div{
	
	text-align:right;
	margin:10px;
	margin-bottom:5px;
	margin-top:5px;
	
}

.home_link_button{
 	background: none;
    border: none;
    display: inline;
    font-size:0.8em;
    margin: 0;
    padding: 0;
    padding-right:10px;
    outline: none;
    outline-offset: 0;  
    color: white;
    cursor: pointer;
    text-decoration: underline;
}

.link_button{
 	background:none;
    border:none;
    display:inline;
    font-size:0.6em;
    margin:0;
    padding:0;
    outline:none;
    outline-offset:0;  
    color:blue;
    cursor:pointer;
    text-decoration:underline;
}


/*Questionnaire buttons*/
.questionnaire_button {
	border:2px #909090;
	border-style:outset;
	background-color:#612d70; 
	max-width:150px;
	font-size:0.6em;
	padding:5px;
	display:block;
	color:#FFFFFF;
	cursor: pointer;
}



/* class that is added to the button when pressed via javascript */
.questionnaire_button_active {
	border:2px #909090;
	border-style:inset;
	background-color:#872b8c; 
	font-weight:bold;
}


/* Navigation styling */

.navigation_button {
	border:2px #909090;
	border-style:outset;
	background-color:#808080; 
	
	max-width:100px;
	width:30%;
	font-weight:bold;
	padding:5px;
	display:block;
	color:#FFFFFF;
}

.navigation_button_hover {
	cursor:pointer;
}

/* a new class that is added to the button when pressed via javascript */
.navigation_button_active {
	border: 2px #909090;
	border-style:inset;
	background-color:#872b8c; 
}

#next_button { 
	float:right; 
}


#back_button { 
	float:left; 
}

.close_button {
	float:right;
}


form {
	overflow:auto;
	min-height:100px;
	margin-bottom:0px;   
}

form.questionnaire_list_form{
	overflow:auto;
	height:auto;
	min-height:0px;
    width:50%; 
    margin:0 auto;
}

form.link_form{
	overflow:auto;
	height:auto;
    margin:0 auto;
}

form#home_form{
	float:left;
	min-height:0px;
}


#questionnaire_info {
	display:inline-block;
	float: right;
	font-style:italic;
	font-size:0.8em;
	font-weight:normal;
}


#participant_id {
	display:inline-block;
	float: right;
	font-style:italic;
	/*font-size:0.8em;*/
	font-size:0.4em;
	font-weight:normal;
}

#questionnaire_version {
	display:inline-block;
	float: left;
	font-style:italic;
	/*font-size:0.7em;*/
	font-size:0.4em;
	font-weight:normal;
}



/* Section styling */

.section {
	font-family:Verdana, Geneva, sans-serif;
	background-color:#EDE6EF;
	
	border:3px ridge #637595;
}


.section_title {
	background-color:#183569;
	color:#FFFFFF;
	/*font-size:1.8em;*/
	font-size:0.9em;
	font-weight:bold;
	padding: 5px;
}


.section_div {
	padding:5px;
	/*font-size:1.4em;*/
	font-size:0.7em;
}


.section_header{
	font-weight:bold;
	/*font-size:1.8em;*/
	font-size:0.9em;
}

.section_subheader{
	font-weight:bold;
	/*font-size:1.5em;*/
	font-size:0.7em;
}


.section_footer{
	font-style:italic;	
	font-size:80%;
}


.last_section_div{
	text-align:center;
	font-weight:bold;
	/*font-size:2em;*/
	font-size:1em;
	min-height:400px;
	/*min-height:50%;   doesn't work in firefox??*/
}

.last_section_footer{
	font-weight:normal;
}

/* QuestionGroup styling */

.questiongroup_div {
	border:1px solid #B0B0B0 ;
	padding:5px;
	margin-top:5px;
	/*font-size:1.4em;*/
	font-size:0.7em;
}


.questiongroup_title{
	font-weight:bold;
}

.questiongroup_header{
	font-weight:bold;
}

.questiongroup_footer{
	font-style:italic;	
	font-size:80%;
}


/* TextNode styling */

.textnode_header{
	font-weight:bold;
}

.textnode_footer{
	font-style:italic;	
	font-size:80%;
}



/* Question styling */

.question_header{
	font-weight:bold;
}

.question_footer{
	font-style:italic;	
	font-size:80%;
}


/* Options styling */

.option_header{
	font-weight:bold;
}

.option_footer{
	font-style:italic;	
	font-size:80%;
}


/* General classes */

label{
	cursor:pointer;
}

label[disabled]{
	cursor:default;
}

.header{
	text-align:center;
	font-weight:bold;
	font-style:italic;
	background-color:#183569;
	color:#FFFFFF;
}

.header2{
	text-align:center;
	font-weight:bold;
	font-style:italic;
	background-color:#234d99;
	color:#FFFFFF;
}

.header3{
	text-align:center;
	font-weight:bold;
	font-style:italic;
	background-color:#2e65c9;
	color:#FFFFFF;
}

.header4{
	text-align:center;
	font-weight:bold;
	font-style:italic;
	background-color:#5987d9;
	color:#FFFFFF;
}

.subheader{
	text-align:center;
	font-style:italic;
	background-color:#183569;
	color:#FFFFFF;
}

.subheader2{
	text-align:center;
	font-style:italic;
	background-color:#234d99;
	color:#FFFFFF;
}

.subheader3{
	text-align:center;
	font-style:italic;
	background-color:#2e65c9;
	color:#FFFFFF;
}

.subheader4{
	text-align:center;
	font-style:italic;
	background-color:#5987d9;
	color:#FFFFFF;
}


.questiontext_header{
	font-style:italic;
}

.bordered {
	border:1px solid black;
}

.bordered_2 {
	border:2px solid black;
}

.topborder{
	border-top:1px solid black;
}

.bottomborder{
	border-bottom:1px solid black;
}

.leftborder{
	border-left:1px solid black;
}

.rightborder{
	border-right:1px solid black;
}


.textalign_center {
	text-align:center;
}

.textalign_right {
	text-align:right;
}

.textalign_left {
	text-align:left;
}


.fontweight_bold {
	font-weight:bold;
}

.fontstyle_italic {
	font-style:italic;
}

.textdecor_underline {
	text-decoration:underline;
}
/*add more for other font properties*/



.backgoundcolor_183569{
	background-color:#183569;
}

.color_FFFFFF{
	color:#FFFFFF;
}


/*to show single line to the borders*/
/*table {
	border-collapse:collapse;
}*/

table {
	border-spacing:0pt;
}


.width_80{
	width:80px;
}

.width_100{
	width:100px;
}

.width_300{
	width:300px;
}

.maxwidth_50{
	max-width:50px;
}

.maxwidth_100{
	max-width:100px;
}

.maxwidth_200{
	max-width:200px;
}

.maxwidth_300{
	max-width:300px;
}

.maxwidth_500{
	max-width:500px;
}

.maxwidth_1000{
	max-width:1000px;
}

.maxwidth_70pc{
	max-width:70%;
}

.minwidth_60{
	min-width:60px;
}

.minwidth_100{
	min-width:100px;
}

.minwidth_200{
	min-width:200px;
}

.minwidth_300{
	min-width:300px;
}


table.alt_color tr:nth-child(odd){
	background-color:#D5CFD7;
}

input[type=text] {
	border-style:inset;	
	border-width: 2px; 
	padding: 1px 5px 1px 5px;
}

input[type=password] {
	border-style:inset;	
	border-width: 2px; 
	padding: 1px 5px 1px 5px;
}

textarea{
	border-style:inset;	
	border-width: 2px; 
	padding: 1px 5px 1px 5px;
}

.vertical_slider{
 	-webkit-appearance: slider-vertical;    /*for chrome*/
}


/*input[type=text]:focus{ 

	border-style: solid; 
	border-color: black;
}*/

/*use bigger radio buttons instead of the default ones*/

input[type=radio] {  
    display: none;  
} 


/*span is after the radio button. If it is before, there is no way in css3 to select it (cannot select a parent with a specific child). It needs Javascript?*/
span.radio:before {  
    content: "";  
    display: inline-block;  
    width: 18px;  
    height: 18px;  
   	margin-right: 5px;  
    background-color: #aaa;  
    box-shadow: inset 0px 2px 3px 0px rgba(0, 0, 0, .3), 0px 1px 0px 0px rgba(255, 255, 255, .8);  
    border-radius: 10px;  
}  


input[type=radio]:checked + span.radio:before {  
    content: "\2022";  /*"\2713";   tick. use 20px font-size*/  
    color: black; /*#EDE6EF; /*#f3f3f3;*/  
    font-size: 25px;
    text-align: center;  
    line-height: 14px;  
}  



/* --------to use images instead of radio buttons--------------

#id856_1 {
	display:none;
}

#id856_2 {
	display:none;
}

#id856_1:checked + img {
	border:2px solid #f00;
}

#id856_2:checked + img {
	border:2px solid #f00;
}

#id845_1{
	display:none;
}


#id845_1:checked + img{
	border:2px solid #f00;
}

#id845_2{
	display:none;
}

#id845_2 + img {
	height:50px;
	width:50px;
}

#id845_1 + img {
	height:50px;
	width:50px;
}

#id845_2:checked + img{	
	border:2px solid #f00;
}

----------------------------------*/

td {
	padding:5px;
}

/*table {
	
	table-layout: fixed;
}*/


/* Reverse text writing
.reverse{
	
	direction: rtl; 
	unicode-bidi: bidi-override;

}

input[type=text] {
    direction: rtl;
    unicode-bidi: bidi-override;
}

*/

/*.question_id_div {
	margin:0;
	border:0;
}

.input_div {
	
	margin:0;
}*/


span.footer{
	float:right;
}

span.visited{
	float:right;
}

.error_div {
	width:auto;
	color: #D8000C;
    background-color: #FFBABA;
    padding:10px 40px;
    border-radius:25px;

}

.warning_div {
	width:auto;
	color:#9F6000;
	background-color:#FEEFB3;
	padding:10px 40px;
    border-radius:25px;
	/*display:inline;*/
}


.error_summary_div{
	width:auto;
	color: #D8000C;
    background-color: #FFBABA;
    border:solid 2px #D8000C;
    padding:10px 40px;
    border-radius:25px;
}

.warning_summary_div{
	width:auto;
	color:#9F6000;
	background-color:#FEEFB3;
	border:solid 2px #9F6000;
    padding:10px 40px;
    border-radius:25px;
}

.error_question{
	background-color:#FFBABA;
}

.warning_question{
	background-color:#FEEFB3;
}

[hide] {
	background-color:#98D6D6;
	/*#A0FFFF;*/
	
}


input[type='button'][disabled] {
  opacity: 0.5;
  cursor:default;
}

</style>