function edit_mode(tableid, flag){
	
	$(function() {
		if (flag == 0) {
			$(tableid + " td").each( function(){
				var val = $(this).children("input").attr("value");
				$(this).html(val);
			});
		}
		else {
			$(tableid + " td").each( function(){
				var name = $(this).attr("id");
				$(this).html('<input type="text" id="' + name + '" name = "' + name + '" value="' + $(this).html() + '" />');
			});
		}
		
	});
}