$(document).ready(function(){

	var minValue = 1;
	var maxValue = 10;
	var currentNValue=$("#nInput").attr("value");
	var currentKValue=$("#kInput").attr("value");
	$( "#nSlider" ).slider({ min: minValue, max:maxValue,value: currentNValue });
	$( "#kSlider" ).slider({ min: minValue, max:maxValue,value: currentKValue });
	$("#nValue").html(currentNValue);
	$("#kValue").html(currentKValue);
	
	

	$( "#nSlider" ).on( "slide", function( event, ui ) {
		$("#nValue").html(ui.value);
		$("#nInput").attr("value",ui.value);
		if (ui.value < $( "#kSlider" ).slider( "value" )){
			$( "#kSlider" ).slider( "value", ui.value );
			$( "#kValue" ).html(ui.value);
			$( "#kInput" ).attr("value",ui.value);
		}
			
	});

	$( "#kSlider" ).on( "slide", function( event, ui ) {
		$("#kValue").html(ui.value);
		$("#kInput").attr("value",ui.value);
		if (ui.value > $( "#nSlider" ).slider( "value" )){
			$( "#nSlider" ).slider( "value", ui.value );
			$( "#nValue" ).html(ui.value);
			$( "#nInput" ).attr("value",ui.value);
		}
			
	});



});