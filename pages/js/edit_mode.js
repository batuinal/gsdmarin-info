function edit_mode(tableid){
	$(function() {
		$(tableid + " .selected td").each( function(){
			var name = $(this).attr("id");
			if($(this).html() == $(this).text())
				$(this).html('<input type="text" id="' + name + '" name = "' + name + '" value="' + $(this).html() + '" />');
		});
	});
}