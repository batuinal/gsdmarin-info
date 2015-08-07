ridx = -1;

function edit_mode(tname, tobj, cols){
	$(function() {
		$("#" + tname + " td").each( function(){
			var name = $(this).attr("id");
			if($(this).html() == $(this).text())
				$(this).html('<input type="text" id="' + name + '" name = "' + name + '" value="' + $(this).html() + '" />');
		});

		$("#edit_mode_" + tname).hide();
		
		$("#buttons_" + tname).append('<button id="cancel_' + tname +'">Cancel Edit</button>\n');
		$("#buttons_" + tname).append('<button id="add_row_' + tname +'">Add Row</button>\n');
		$("#buttons_" + tname).append('<button id="delete_row_' + tname +'">Delete Row</button>\n');
		$("#buttons_" + tname).append('<button id="submit_' + tname +'">Submit</button>\n');
		
		$("#delete_row_" + tname).click( function () { tobj.rows(".selected").remove().draw( false );} );
		
		$("#add_row_" + tname).click( function () {
				var rin = [];
				for (i = 0; i < cols.length; i++){
					var idname = ridx + "_" + cols[i]
					rin.push('<input type="text" id="' + idname + '" name="' + idname + '" value="" />');
				}
				tobj.row.add(rin).draw();
				ridx--;
			});
		
		$("#cancel_" + tname).click( function () {
			request('GET','/view_table',['pageid'],[document.getElementById('pageid').getAttribute('value')]);
		});
		
		$("#submit_" + tname).click( function () {
			$("#buttons_" + tname).hide();
			
			var data = $("#" + tname + " input").serializeArray();
			data.push({ name: 'table', value: tname });
			$.post("/submit_table",data, function (response) {
				console.log(response);
			});
			
			request('GET','/view_table',['pageid'],[document.getElementById('pageid').getAttribute('value')]);
		});
		
	});
}