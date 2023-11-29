// $(document).ready(function(){
// 	$('#like_count').html("");
// 	$('#like_button').attr("value","Like:)");
// 	$('#like_button').click(function(){
		
// 		$.get('/graphs/like/', function(data){
// 	       $('#like_count').html(data);
// 	       $('#like_button').attr("value","Moar!");
//    		});
// 	});

// 	$('#build_graphs_button').click(function(){
// 		$('#like_button').attr("value","Like:)");
		
// 		var varN = $("#nInput").attr("value")
// 		var varK = $("#kInput").attr("value")
// 		$('#like_count').html("");
// 		$.get('/graphs/build_ajax/', {N: varN, K: varK}, function(){

// 			$(".img_table_cell a img").each(function(i){
// 				// refresh all images
// 				d = new Date();
// 				var imgsrc = $(this).attr("src");
// 				console.log(imgsrc);
// 				if (imgsrc.indexOf("?")!=-1)
// 					imgsrc=imgsrc.substr(0,imgsrc.indexOf("?"));
// 				console.log(imgsrc);
// 		        $(this).attr("src", imgsrc+"?"+d.getTime());

// 			});
		   
//    		});
// 	});

// });
$(document).ready(function(){
    $('#like_count').html("");
    $('#like_button').attr("value","Like:)");
    $('#like_button').click(function(){
        $.get('/graphs/like/', function(data){
            $('#like_count').html(data);
            $('#like_button').attr("value","Moar!");
        });
    });

    $('#build_graphs_button').click(function(){
        $('#like_button').attr("value","Like:)");

        var varN = $("#nInput").attr("value")
        var varK = $("#kInput").attr("value")
        $('#like_count').html("");

        // Use AJAX to reload the entire page
        $.get('/graphs/build_ajax/', {N: varN, K: varK}, function(){
			location.reload();  // Reload the entire page
        });
    });
});
