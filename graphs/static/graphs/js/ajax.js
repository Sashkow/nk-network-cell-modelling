$(document).ready(function(){

	$('#like_button').click(function(){
		
		$.get('/graphs/like/', function(data){
	       $('#like_count').html(data);
   		});
	});

	$('#build_graphs_button').click(function(){
		var varN = $("#nInput").attr("value")
		var varK = $("#kInput").attr("value")
			
		$.get('/graphs/build_ajax/', {N: varN, K: varK}, function(){

			$(".img_table_cell a img").each(function(i){
				// refresh all images
				d = new Date();
				var imgsrc = $(this).attr("src");
				console.log(imgsrc);
				if (imgsrc.indexOf("?")!=-1)
					imgsrc=imgsrc.substr(0,imgsrc.indexOf("?"));
				console.log(imgsrc);
		        $(this).attr("src", imgsrc+"?"+d.getTime());

			});
		   
   		});
	});

});