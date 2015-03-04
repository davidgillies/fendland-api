
var FORM_HAS_CHANGED = false;

$(function(){	
   	
	//To keep the session alive send every 5 minutes an empty request to the server. Use this if you want the session never to expire
	//window.setInterval('keepSessionAlive()', 300000);
		    
	$.post('/fenland/next_section').done(function(data) {
		
	
		$('#page_content').append(data);
		setHeight();
		
		$('[disable="yes"]').each(function(){
			
			$(this).find('*').each(function () { $(this).attr('disabled', true); });
		}); 
		
					
		$('input').change(conditional_questions);
		
		$("input, select, textarea").change(function(){
			FORM_HAS_CHANGED = true;
		
		});
		
		//$("option").click(conditional_questions);		//the click event of option does not fire in chrome. So use the select-->change event instead
		$('select').change(conditional_questions_dropdown);
		$('input').keyup(conditional_questions_textbox);
		
		//if the questionnaire is already submitted, disable the form
		$('.submitted_form input').attr('disabled',true);
		$('.submitted_form textarea').attr('disabled',true);
		$('.submitted_form select').attr('disabled',true);
		
		$('.disabled input').attr('disabled',true);
		$('.disabled textarea').attr('disabled',true);
		$('.disabled select').attr('disabled',true);
		
		//if the section is the pin section, rename the next button to submit and show some information
		$('div').find('.section').each(function () {
			if($('div > div').hasClass('pin_section_div') && !$('div > div').hasClass('submitted_section')){   //if the questionnaire was already submitted, do not change next button to submit
				if(!$('*form').hasClass('error_summary_div')) {  
					$('*#next_button').attr('value','Submit'); 
					$('*#next_button').addClass('close_button');
					$('*.close_button').attr('title','Press this button to submit your answers. You will not be able to change your answers after you submit your answers');
					//$('span.footer').html('Please press the Submit button to save your answers.<br>Please note that you will not be able to change your answers after you press the Submit button.');
					$('*#submitted').attr('value','yes');
				}
			}
			
			//if the section is the last section, disable every button
			if($('div > div').hasClass('last_section_div') && !$('div > div').hasClass('submitted_section')){
				$('*#back_button').attr('disabled','disabled');
				$('*#back_button').attr('title','');
				//$("*#back_button").hide();
				//$("*.close_button").attr("disabled","disabled");  //If just disable it, it will be enabled again after the timeout below. So better hide it.
				$('*.close_button').attr('title', '');
				$('*.close_button').hide();
				$('span.footer').addClass('visited');
				$('span.footer').removeClass('footer');  //remove this class so that the next_button() will not pick this span and put the text again.
				$('span.visited').html('Select "Back to main menu" on top to go back to the questionnaire list.');
			}
			
		});
		
		if($(document).find('.last_section_div')[0] !== undefined){
			$('#page_meter').hide();
		}
					
		//$("table.alt_color tr:odd").css("background-color", "#D5CFD7");

	});
	 

	
	$('.navigation_button').mousedown(function() {
		
		$(this).addClass('navigation_button_active');
		
	});
	

	$('.navigation_button').mouseup(function() {
		
		$(this).removeClass('navigation_button_active');
		
	});
	
	
	$('.questionnaire_button').mousedown(function() {
		
		$(this).addClass('questionnaire_button_active');
		
	});
	

	$('.questionnaire_button').mouseup(function() {
		
		$(this).removeClass('questionnaire_button_active');
		
	});
	
	
	$('#next_button').click(function() {
		
		FORM_HAS_CHANGED = false;
		
				
		if($('#next_button').hasClass('close_button')){
		
			if(confirm('Are you sure you want to submit your answers? Press CANCEL if you wish to review your answers or if you want a researcher to review your answers before you submit the questionnaire. You will not be able to change your answers after you press OK.')){
				next_operation();
				var mybutton = this;
				
				mybutton.disabled = true;
				setTimeout(function() {
					mybutton.disabled = false;
				}, 1000);
			}
		} else {
			next_operation();
			var mybutton = this;
			
			mybutton.disabled = true;
			setTimeout(function() {
				mybutton.disabled = false;
			}, 1000);
		}
				

	});
	
	

	$('#back_button').click(function() {
		
		var error_div = $(document).find('.error_summary_div')[0];
		var warning_div = $(document).find('.warning_summary_div')[0];
		var submitted_form = $(document).find('.submitted_form')[0];
		
		if ((FORM_HAS_CHANGED || error_div !== undefined || warning_div !== undefined) && submitted_form === undefined) {
			if(confirm('Are you sure you want to leave this section? The changes you made to this section will be lost! If you want to save your answers to the current section you need to complete it correctly and press Next.')){
				back_operation();
			}
		} else {
			back_operation();
		}
		
		var mybutton = this;
		
		mybutton.disabled = true;
		setTimeout(function() {
			mybutton.disabled = false;
		}, 1000);
			
	});
	
	$('#home_button').click(function(event) {
		var error_div = $(document).find('.error_summary_div')[0];
		var warning_div = $(document).find('.warning_summary_div')[0];
		var submitted_form = $(document).find('.submitted_form')[0];
			
		if ((FORM_HAS_CHANGED || error_div !== undefined || warning_div !== undefined) && submitted_form === undefined) {
			if(!confirm('Are you sure you want to leave this section? The changes you made to this section will be lost! If you want to save your answers to the current section you need to complete it correctly and press Next.')){
				event.preventDefault();
			}
		}
	});
	
	$('#logout_button').click(function(event) {
		var error_div = $(document).find('.error_summary_div')[0];
		var warning_div = $(document).find('.warning_summary_div')[0];
		var submitted_form = $(document).find('.submitted_form')[0];

		if ((FORM_HAS_CHANGED || error_div !== undefined || warning_div !== undefined) && submitted_form === undefined) {
			if(!confirm('Are you sure you want to leave this section? The changes you made to this section will be lost! If you want to save your answers to the current section you need to complete it correctly and press Next.')){
				event.preventDefault();
			}
		}
		
	});
	
	
	
	//Use this function if you don't have the pin section before the thank you section
	/*$(document).on("click", ".close_button", function(){   //use this because this class is dynamically added to the button (it is not like that when you load the page initially)
	//$(".close_button").click(function() {
		if(!$("*form").hasClass("error_summary_div")) {  
			$("*#back_button").attr("disabled","disabled");
			$("*#back_button").attr('title','');
			//$("*#back_button").hide();
			$(this).attr("disabled","disabled");
			$(this).attr('title', '');
			//$(this).hide();
			$("span.footer").addClass("visited");  
			$("span.footer").removeClass("footer");  //remove this class so that the next_button() will not pick this span and put the text again.
			$("span.visited").html("");
		
		}
		
		//window.close();
		
	});*/
	
	
	$('#close_button').click(function() {
		
		window.close();
		
	});
	
	
	 $('.popup').click(function() {
		 var NWin = window.open($(this).prop('href'), '', 'height=800,width=800');
		
		 if (window.focus){
		      NWin.focus();
		  }
		 
		  return false;
	 });
	 
	
	 
     $( window ).scroll(moveScroll);
     
     $( window ).resize(setWidth);
     
     $( window ).resize(setHeight);
     
	
     //Can't use this as in Firefox there is a known bug that the message for the onbeforeunload is fixed and cannot be changed.
     //So I use separate code for back button/link and logout button/link but in this way I do not catch the pressing of the browser's back button.
     /*window.onbeforeunload = function() {
    	var error_div = $(document).find('.error_summary_div')[0];
		var warning_div = $(document).find('.warning_summary_div')[0];
		var submitted_form = $(document).find('.submitted_form')[0];
			
		if ((FORM_HAS_CHANGED || error_div !== undefined || warning_div !== undefined) && submitted_form === undefined) {
			return 'Are you sure you want to leave this section? The changes you made to this section will be lost! If you want to save your answers to the current section you need to complete it correctly and press Next.';
		}	
	};*/
     
     
});
 

//to open questionnaire info in a new window tab
/*function windowpop(url) {
	
	window.open(url);
};*/


// sets the height of the form so that it is based on the window size. This is done for the next and back buttons to be visible all the time even when resizing the window.
function setHeight() {

    //console.log("window.innerHeight="+window.innerHeight);
    //console.log("document.body.clientHeight="+document.body.clientHeight);
    //console.log("document.documentElement.clientHeight="+document.documentElement.clientHeight);
    $('form#questionnaire_form').css("height", window.innerHeight-220+"px");
   
}


function next_operation(){

	console.log( $('form').serialize() );

	var str = $('form').serializeArray();
		
	$('#page_content').fadeOut(250);
	
	$.post('/fenland/handle_results', str).done(function(data) {
		
		$('#page_content').empty();
		$('#page_content').append(data);
		setHeight();
		$('#page_content').fadeIn(250);
		$('form#questionnaire_form').scrollTop(0,0);   //to make the form scroll to the top as in firefox it did not
		
		//to disable all the fields marked as disable="yes")
		 $('[disable="yes"]').each(function(){
			
			$(this).find('*').each(function () { $(this).attr('disabled', true); });
		}); 
		
		$("input, select, textarea").change(function(){
			FORM_HAS_CHANGED = true;
		});
		
		$('input').change(conditional_questions);
		//$("option").click(conditional_questions);		//the click event of option does not fire in chrome. So use the select --> change event instead
		$('select').change(conditional_questions_dropdown);
		$('input').keyup(conditional_questions_textbox);
		//$("table.alt_color tr:odd").css("background-color", "#D5CFD7");
		
		//if the questionnaire is already submitted, disable the form
		$('.submitted_form input').attr('disabled',true);
		$('.submitted_form textarea').attr('disabled',true);
		$('.submitted_form select').attr('disabled',true);
		
		$('.disabled input').attr('disabled',true);
		$('.disabled textarea').attr('disabled',true);
		$('.disabled select').attr('disabled',true);
					
		//if the section is the pin section, rename the next button to submit and show some information
		$('div').find('.section').each(function () {
			if($('div > div').hasClass('pin_section_div') && !$('div > div').hasClass('submitted_section')){   //if the questionnaire was already submitted, do not change next button to submit
				if(!$('*form').hasClass('error_summary_div')) {  
					$('*#next_button').attr('value','Submit'); 
					$('*#next_button').addClass('close_button');
					$('*.close_button').attr('title','Press this button to submit your answers. You will not be able to change your answers after you submit your answers');
					$('*#submitted').attr('value','yes');
				}
			}
			
			//if the section is the last section, disable every button
			if($('div > div').hasClass('last_section_div') && !$('div > div').hasClass('submitted_section')){
				$('*#back_button').attr('disabled','disabled');
				$('*#back_button').attr('title','');
				//$("*#back_button").hide();
				//$("*.close_button").attr("disabled","disabled");  //If just disable it, it will be enabled again after the timeout below. So better hide it.
				$('*.close_button').attr('title', '');
				$('*.close_button').hide();
				$('span.footer').addClass('visited');
				$('span.footer').removeClass('footer');  //remove this class so that the next_button() will not pick this span and put the text again.
				$('span.visited').html('Select "Back to main menu" on top to go back to the questionnaire list.');
			}
			
			//To hide the progress bar at the last page even if the questionnaire is submitted
			if($('div > div').hasClass('last_section_div')){
				$('#page_meter').hide();
			}
			
		});	 
		
	});
	
}



function back_operation() {
	
	$('#page_content').fadeOut(250);
	
	$.post('/fenland/previous_section').done(function(data) {
		
		$('#page_content').empty();
		$('#page_content').append(data);
		setHeight();
		$('#page_content').fadeIn(250);
		
		$('form#questionnaire_form').scrollTop(0,0);   //to make the form scroll to the top as in firefox it did not
		
		//to disable all the fields marked as disable="yes")
		 $('[disable="yes"]').each(function(){
				
			$(this).find('*').each(function () { $(this).attr('disabled', true); });
		}); 
	
		 $("input, select, textarea").change(function(){
				FORM_HAS_CHANGED = true;
		});
		 
		$('input').change(conditional_questions);
		//$("option").click(conditional_questions);		//the click event of option does not fire in chrome. So use the select --> change event instead
		$('select').change(conditional_questions_dropdown);
		$('input').keyup(conditional_questions_textbox);

		//$("table.alt_color tr:odd").css("background-color", "#D5CFD7");
		
		//if the questionnaire is already submitted, disable the form
		$('.submitted_form input').attr('disabled',true);
		$('.submitted_form textarea').attr('disabled',true);
		$('.submitted_form select').attr('disabled',true);
		
		$('.disabled input').attr('disabled',true);
		$('.disabled textarea').attr('disabled',true);
		$('.disabled select').attr('disabled',true);
		
		$('div').find('.section').each(function () {
			if($('div > div').hasClass('pin_section_div') && !$('div > div').hasClass('submitted_section')) { 
				$('*#next_button').attr('value','Submit'); 				
				$('*#next_button').addClass('close_button');
				$('*.close_button').attr('title','Press this button to submit your answers. You will not be able to change your answers after you press this button');
				$('*#submitted').attr('value','yes');
			} else {
				$('*.close_button').attr('value','Next >>');  
				$('*.close_button').removeClass('close_button');
				$('*#next_button').attr('title','Press this button to go to the next section');
				$('span.footer').html('');
			}
		});	 
	});
	FORM_HAS_CHANGED = false;
}

//Used to keep a session alive. Send an empty ajax request to the server. Set this up at the beginning of the load function with setIntervel.
function keepSessionAlive() {
    $.post('/fenland/ping');
}







//To freeze the headers of a table when scrolling
function moveScroll(){

	var checked = [];
	var textvals = [];
	
	var table = $('table.freeze_headers');
	var scroll = table.scrollTop();
	if(table.position() !== undefined){
		var anchor_top = table.position().top - $('form#questionnaire_form').position().top;
	
		var top = $('form#questionnaire_form').position().top - $(window).scrollTop()+9;
		
		if (scroll>anchor_top){
			
		    clone_table = $('#clone');
		   
		    if(clone_table.length == 0){
		    	
		    	//get the checked values of the radio buttons before you insert the clone table or it will lose them
		        $('table.freeze_headers input[type="radio"]').each(function(index) {
		              checked[index] = this.checked;
		        });
		    
		        //get the values of the textboxes before you insert the clone table or it will lose them
		       $('table.freeze_headers input[type="text"]').each(function(index) { 
		              textvals[index] = $(this).val();
		        });
		       
		       //add each()... for other types of inputs (checkboxes etc.)
		    	
		        clone_table = $('table.freeze_headers').clone().attr('id', 'clone').insertAfter($('table.freeze_headers'));
		        clone_table.removeClass('freeze_headers');
		        clone_table.css('position', 'fixed');
		        clone_table.css('pointer-events', 'none');
		        clone_table.css('z-index', '10');
		       
		        $('#clone').css({visibility:'hidden'});
		        $('#clone .fixheader').css({visibility:'visible'});
		       
		        //reassign the values of the cheched radio buttons as they were lost but the insertion of the clone table
		        $('table.freeze_headers input[type="radio"]').each(function(index) {
	                this.checked = checked[index];
	            });
		        
		      //reassign the values of the textboxes as they were lost but the insertion of the clone table
		        $('table.freeze_headers input[type="text"]').each(function(index) {
		        	$(this).val(textvals[index]);
		        });
		        
		        //re-assign the values of other input types (checkboxes etc.)
		        
		    } else {
		    	
		    	clone_table.css('top', top + 'px');
		    }
		  
	        setWidth();
	          
		    $('#clone').show();
		    $('#clone').css('z-index', '10');
		    
		   
	    } else {
	    	
	    	//$("#clone").remove();  //problem, it looses the values
	    	//$("#clone").hide();   //problem, it looses the alignment with the table columns
	    	
	    	//put it at the back
	    	$('#clone').css('z-index', '-10');
	    	
	    }
	}
	
}


function setWidth() {
	var table = $('table.freeze_headers');
	var border_width = parseInt(table.css('border-width'));
	
    if ( navigator.userAgent.match(/Chrome/) ) { // for Chrome
        $('#clone').width( $('table.freeze_headers').width() + border_width*2 );
    }
    else {

    	$('#clone').width( $('table.freeze_headers').width());
    }
}


//to hide/show or enable/disable questions RADIO BUTTONS
	function conditional_questions(){
	
		//text input
		//if($(this).attr('type')=='text'){
			if($(this).attr('type')=='text'){
				if($(this).data('showanswered')){
					var showq=$(this).data('showanswered').split(' ');
					if($(this).val().length > 0) {
						
						for ( var i = 0; i < showq.length; i++ ) {
							$('[conditional=' + showq[i] + ']').show();														
						}
					} 
				}
				
				if($(this).data('shownotanswered')){
					var showq=$(this).data('shownotanswered').split(' ');
					if($(this).val().length == 0) {
						
						for ( var i = 0; i < showq.length; i++ ) {
							$('[conditional=' + showq[i] + ']').show();														
						}
					} 
				}
				
				if($(this).data('hideanswered')){
					var hideq=$(this).data('hideanswered').split(' ');
					if($(this).val().length > 0) {
				
						for ( var i = 0; i < hideq.length; i++ ) {
			
							$('[conditional=' + hideq[i] + ']').hide();
							$('[conditional=' + hideq[i] + ']').find(':input').each(function() {
								switch(this.type) {
									case 'text':
									case 'textarea':
										$(this).val('');
										break;
									case 'checkbox':
									case 'radio':
										this.checked = false;		
									//add other cases if needed	
								}
							});
							$('[conditional=' + hideq[i] + ']').find('select').each(function() {
								$(this).prop('selectedIndex',0);
								$(this).change();
							});
						}
					}
				}
				
				if($(this).data('hidenotanswered')){
					var hideq=$(this).data('hidenotanswered').split(' ');
					if($(this).val().length == 0) {
				
						for ( var i = 0; i < hideq.length; i++ ) {
			
							$('[conditional=' + hideq[i] + ']').hide();
							$('[conditional=' + hideq[i] + ']').find(':input').each(function() {
								switch(this.type) {
									case 'text':
									case 'textarea':
										$(this).val('');
										break;
									case 'checkbox':
									case 'radio':
										this.checked = false;		
									//add other cases if needed	
								}
							});
							$('[conditional=' + hideq[i] + ']').find('select').each(function() {
								$(this).prop('selectedIndex',0);
								$(this).change();
							});
						}
					}
				}
				
								 
				if($(this).data('enableanswered')){
					var enableq=$(this).data('enableanswered').split(' ');
					if($(this).val().length > 0) {
						
						for ( var i = 0; i < enableq.length; i++ ) {
							$('[conditional=' + enableq[i] + ']').find('*').each(function () { $(this).attr('disabled', false); });	
						}
						
					} 
				}
				
				if($(this).data('enablenotanswered')){
					var enableq=$(this).data('enablenotanswered').split(' ');
					if($(this).val().length == 0) {
						for ( var i = 0; i < enableq.length; i++ ) {
							$('[conditional=' + enableq[i] + ']').find('*').each(function () { $(this).attr('disabled', false); });	
						}
						
					} 
				}
				
				
				if($(this).data('disableanswered')){
					var disableq=$(this).data('disableanswered').split(' ');
					if(($(this).val().length > 0)){
						for ( var i = 0; i < disableq.length; i++ ) {
							$('[conditional=' + disableq[i] + ']').find('*').each(function () { $(this).attr('disabled', true); });
							$('[conditional=' + disableq[i] + ']').find(':input').each(function() {
								switch(this.type) {
									case 'text':
									case 'textarea':
										$(this).val('');
										break;
									case 'checkbox':
									case 'radio':
										this.checked = false;
									//add other cases if needed	
								}
							});
							$('[conditional=' + disableq[i] + ']').find('select').each(function() {
								$(this).prop('selectedIndex',0);
								$(this).change();
							});
						}
					}
				}
								 
				if($(this).data('disablenotanswered')){
					var disableq=$(this).data('disablenotanswered').split(' ');
					if(($(this).val().length == 0)){
						for ( var i = 0; i < disableq.length; i++ ) {
							$('[conditional=' + disableq[i] + ']').find('*').each(function () { $(this).attr('disabled', true); });
							$('[conditional=' + disableq[i] + ']').find(':input').each(function() {
								switch(this.type) {
									case 'text':
									case 'textarea':
										$(this).val('');
										break;
									case 'checkbox':
									case 'radio':
										this.checked = false;
									//add other cases if needed	
								}
							});
							$('[conditional=' + disableq[i] + ']').find('select').each(function() {
								$(this).prop('selectedIndex',0);
								$(this).change();
							});
						}
					}
				}
				
			//}
					
			
		} else {		//other input type (not text)

			if($(this).data('show')){
				
				var showq=$(this).data('show').split(' ');
				if($(this).attr('type')=='radio' || ($(this).attr('type')=='checkbox' && $(this).is(':checked'))){
					for ( var i = 0; i < showq.length; i++ ) {
						$('[conditional=' + showq[i] + ']').show();	
					}
					if(($('[conditional=' + showq[0] + ']').find(':input'))[0] !== undefined){ 
						$('[conditional=' + showq[0] + ']').find(':input')[0].focus();		//focus on the first conditional input
					}
				} else if($(this).attr('type')=='checkbox' && !$(this).is(':checked')) {    //if it is a checkbox and it has a show attribute, when unckecked hide again.
					for ( var i = 0; i < showq.length; i++ ) {
						$('[conditional=' + showq[i] + ']').hide();
						$('[conditional=' + showq[i] + ']').find(':input').each(function() {
							switch(this.type) {
							case 'text':
							case 'textarea':
								$(this).val('');
								$(this).keyup();   //to trigger the keyup event on the text box and call the rest for the conditional questions in textboxes
								break;
							case 'checkbox':
							case 'radio':
								this.checked = false;
							//add other cases if needed	
							}
						});
					} 
				}
			}
					
			if($(this).data('hide')){
			
				var hideq=$(this).data('hide').split(' ');
				for ( var i = 0; i < hideq.length; i++ ) {
					$('[conditional=' + hideq[i] + ']').hide();
					$('[conditional=' + hideq[i] + ']').find(':input').each(function() {
						switch(this.type) {
						case 'text':
						case 'textarea':
							$(this).val('');
							$(this).keyup();   //to trigger the keyup event on the text box and call the rest for the conditional questions in textboxes
							break;
						case 'checkbox':
						case 'radio':
							this.checked = false;
						//add other cases if needed	
						}
					});
					$('[conditional=' + hideq[i] + ']').find('select').each(function() {
						$(this).prop('selectedIndex',0);
						$(this).change();   //to triger the change event on dropdowns to reset the conditional questions for dropdowns
					});
					
					
					//remove the warnings
					$('[conditional=' + hideq[i] + ']').find('td.warning_question').each(function() {
						$(this).removeClass('warning_question');
					});
					
					$('[conditional=' + hideq[i] + ']').find('.warning_div').each(function() {
						$(this).remove();
					});
					
					//remove the errors
					$('[conditional=' + hideq[i] + ']').find('td.error_question').andSelf().each(function() {
						$(this).removeClass('error_question');
					});
					
					$('[conditional=' + hideq[i] + ']').find('.error_div').each(function() {
						$(this).remove();
					});
					
					
					/*$('[conditional=' + hideq[i] + ']').parents('.questiongroup_div').find('.error_div').each(function() {
						$(this).remove();
					});*/
		
					
					//remove the warning summary div if there are no more warnings
					var warning_questions = $(document).find('.warning_question');
					var warning_summary_div = $(document).find('.warning_summary_div');
					
					if(warning_questions.length == 0){
						if(warning_summary_div.length != 0) {
							warning_summary_div.remove();
						}
					}
					
					//remove the error summary div if there are no more errors
					var error_questions = $(document).find('.error_question');
					var error_summary_div = $(document).find('.error_summary_div');
					
					if(error_questions.length == 0){
						if(error_summary_div.length != 0) {
							error_summary_div.remove();
						}
					}
					
				}
			}
			
			if($(this).data('enable')){
						
				var enableq=$(this).data('enable').split(' ');
				for ( var i = 0; i < enableq.length; i++ ) {
					$('[conditional=' + enableq[i] + ']').find('*').each(function () { $(this).attr('disabled', false); });	
				}
				if(($('[conditional=' + enableq[0] + ']').find(':input'))[0] !== undefined){ 
					$('[conditional=' + enableq[0] + ']').find(':input')[0].focus();		//focus on the first conditional input
				}
			}
			
			if($(this).data('disable')){
						
				var disableq=$(this).data('disable').split(' ');
				for ( var i = 0; i < disableq.length; i++ ) {
					$('[conditional=' + disableq[i] + ']').find('*').each(function () { $(this).attr('disabled', true); });
					$('[conditional=' + disableq[i] + ']').find(':input').each(function() {
						switch(this.type) {
						case 'text':
						case 'textarea':
							$(this).val('');
							break;
						case 'checkbox':
						case 'radio':
							this.checked = false;
						//add other cases if needed	
						}
					});
					$('[conditional=' + disableq[i] + ']').find('select').each(function() {
						$(this).prop('selectedIndex',0);
						$(this).change();						
					});
				}
			}
		
	}
	}
	
	
	
	//to hide/show or enable/disable questions DROPDOWN
	function conditional_questions_dropdown(){
				
		if($(this).children(':selected').data('show')){

			var showq=$(this).children(':selected').data('show').split(' ');
			for ( var i = 0; i < showq.length; i++ ) {
				
				$('[conditional=' + showq[i] + ']').show();	
			}
			
			if(($('[conditional=' + showq[0] + ']').find(':input'))[0] !== undefined){ 
				$('[conditional=' + showq[0] + ']').find(':input')[0].focus();		//focus on the first conditional input
			}
		}
		
		
		if($(this).children(':selected').data('hide')){
	
			var hideq=$(this).children(':selected').data('hide').split(' ');
			for ( var i = 0; i < hideq.length; i++ ) {
				
				$('[conditional=' + hideq[i] + ']').hide();
				$('[conditional=' + hideq[i] + ']').find(':input').each(function() {
					switch(this.type) {
					case 'text':
					case 'textarea':
						$(this).val('');
						break;
					case 'checkbox':
					case 'radio':
						this.checked = false;
					//add other cases if needed	
					}
				});
				$('[conditional=' + hideq[i] + ']').find('select').each(function() {
					$(this).prop('selectedIndex',0);
					$(this).change();
				});
				
			}
		}
		
		
		if($(this).children(':selected').data('enable')){
			
			var enableq=$(this).children(':selected').data('enable').split(' ');
			for ( var i = 0; i < enableq.length; i++ ) {
				$('[conditional=' + enableq[i] + ']').find('*').each(function () { $(this).attr('disabled', false); });	
			}
			if(($('[conditional=' + enableq[0] + ']').find(':input')[0]) !== undefined){ 
				$('[conditional=' + enableq[0] + ']').find(':input')[0].focus();		//focus on the first conditional input
			} 
		}
		
		
		if($(this).children(':selected').data('disable')){
			
			var disableq=$(this).children(':selected').data('disable').split(' ');
			for ( var i = 0; i < disableq.length; i++ ) {
				$('[conditional=' + disableq[i] + ']').find('*').each(function () { $(this).attr('disabled', true); });
				$('[conditional=' + disableq[i] + ']').find(':input').each(function() {
					switch(this.type) {
					case 'text':
					case 'textarea':
						$(this).val('');
						break;
					case 'checkbox':
					case 'radio':
						this.checked = false;
					//add other cases if needed	
					}
				});
				$('[conditional=' + disableq[i] + ']').find('select').each(function() {
					$(this).prop('selectedIndex',0);
					$(this).change();
				});
			}
		}

	}
	
	////to hide/show or enable/disable questions when keyup event of the text input box
	function conditional_questions_textbox(){
		
		if($(this).attr('type')=='text'){
			if($(this).data('showanswered')){
				var showq=$(this).data('showanswered').split(' ');
				if($(this).val().length > 0) {
					
					for ( var i = 0; i < showq.length; i++ ) {
						$('[conditional=' + showq[i] + ']').show();														
					}
				} 
			}
			
			if($(this).data('shownotanswered')){
				var showq=$(this).data('shownotanswered').split(' ');
				if($(this).val().length == 0) {
					
					for ( var i = 0; i < showq.length; i++ ) {
						$('[conditional=' + showq[i] + ']').show();														
					}
				} 
			}
			
			if($(this).data('hideanswered')){
				var hideq=$(this).data('hideanswered').split(' ');
				if($(this).val().length > 0) {
			
					for ( var i = 0; i < hideq.length; i++ ) {
		
						$('[conditional=' + hideq[i] + ']').hide();
						$('[conditional=' + hideq[i] + ']').find(':input').each(function() {
							switch(this.type) {
								case 'text':
								case 'textarea':
									$(this).val('');
									break;
								case 'checkbox':
								case 'radio':
									this.checked = false;		
								//add other cases if needed	
							}
						});
						$('[conditional=' + hideq[i] + ']').find('select').each(function() {
							$(this).prop('selectedIndex',0);
							$(this).change();
						});
					}
				}
			}
			
			if($(this).data('hidenotanswered')){
				var hideq=$(this).data('hidenotanswered').split(' ');
				if($(this).val().length == 0) {
			
					for ( var i = 0; i < hideq.length; i++ ) {
		
						$('[conditional=' + hideq[i] + ']').hide();
						$('[conditional=' + hideq[i] + ']').find(':input').each(function() {
							switch(this.type) {
								case 'text':
								case 'textarea':
									$(this).val('');
									break;
								case 'checkbox':
								case 'radio':
									this.checked = false;		
								//add other cases if needed	
							}
						});
						$('[conditional=' + hideq[i] + ']').find('select').each(function() {
							$(this).prop('selectedIndex',0);
							$(this).change();
						});
					}
				}
			}
			
							 
			if($(this).data('enableanswered')){
				var enableq=$(this).data('enableanswered').split(' ');
				if($(this).val().length > 0) {
					
					for ( var i = 0; i < enableq.length; i++ ) {
						$('[conditional=' + enableq[i] + ']').find('*').each(function () { $(this).attr('disabled', false); });	
					}
					
				} 
			}
			
			if($(this).data('enablenotanswered')){
				var enableq=$(this).data('enablenotanswered').split(' ');
				if($(this).val().length == 0) {
					
					for ( var i = 0; i < enableq.length; i++ ) {
						$('[conditional=' + enableq[i] + ']').find('*').each(function () { $(this).attr('disabled', false); });	
					}
					
				} 
			}
			
			
			if($(this).data('disableanswered')){
				var disableq=$(this).data('disableanswered').split(' ');
				if(($(this).val().length > 0)){
					for ( var i = 0; i < disableq.length; i++ ) {
						$('[conditional=' + disableq[i] + ']').find('*').each(function () { $(this).attr('disabled', true); });
						$('[conditional=' + disableq[i] + ']').find(':input').each(function() {
							switch(this.type) {
								case 'text':
								case 'textarea':
									$(this).val('');
									break;
								case 'checkbox':
								case 'radio':
									this.checked = false;
								//add other cases if needed	
							}
						});
						$('[conditional=' + disableq[i] + ']').find('select').each(function() {
							$(this).prop('selectedIndex',0);
							$(this).change();
						});
					}
				}
			}
							 
			if($(this).data('disablenotanswered')){
				var disableq=$(this).data('disablenotanswered').split(' ');
				if(($(this).val().length == 0)){
					for ( var i = 0; i < disableq.length; i++ ) {
						$('[conditional=' + disableq[i] + ']').find('*').each(function () { $(this).attr('disabled', true); });
						$('[conditional=' + disableq[i] + ']').find(':input').each(function() {
							switch(this.type) {
								case 'text':
								case 'textarea':
									$(this).val('');
									break;
								case 'checkbox':
								case 'radio':
									this.checked = false;
								//add other cases if needed	
							}
						});
						$('[conditional=' + disableq[i] + ']').find('select').each(function() {
							$(this).prop('selectedIndex',0);
							$(this).change();
						});
					}
				}
			}
			
			
		}
	}
		
	

