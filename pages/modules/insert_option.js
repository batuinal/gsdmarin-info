option_ids = []

function remove_option(id){
		var optid = 'option_' + id;
		var idx = option_ids.indexOf(id);
		option_ids.splice(idx,1);
		$(function(){$('#' + optid).remove();})
}

function insert_option(form_id, values, texts) {
	
	function getid(){
		var id = 0;
		while (option_ids.indexOf(id) > -1){id++}
		option_ids.push(id);
		return id;
	}
	
	if (values.length != texts.length) return;
	
	// Subfunction to convert variable into an injectable string.
	function vtos(val){	return "'" + val + "'";	}
	
	// Subfunction to convert array into an injectable string.
	function atos(array){
		var retstr = "[";
		for (i = 0; i < array.length; i++) {
			if (i)
				retstr += ",";
			retstr += "'" + array[i] + "'";
		}
		retstr += "]";
		return retstr;
	}	
	
	var id = getid();
	
	var optid = 'option_' + id;
	var selectname = 'select_' + id;
	var textboxname = 'textbox_' + id;
	
	var html = '<div class="row cells9" id="' + optid + '">\n';
	html += '<select class="cell colspan4 input-control select" name="' + selectname + '">\n';
	
	for (i = 0; i < values.length; i++){
		html += '<option value="' + values[i] + '"> ' + texts[i] + ' </option>\n';
	}
	
	var insertcmd = '"insert_option(' + vtos(form_id) + ',' + atos(values) + ',' + atos(texts) + ')"';
	
	html += '</select>\n';
	html += '<input class="cell colspan4 input-control text" type="text" name=' + textboxname + '>\n';
	
	// First button is '+', next are '-'
	if (id != 0)
		html += '<button class="cell button mif-minus" type="button" onclick=remove_option(' + id + ')></button>\n';
	else
		html += '<button class="cell button mif-plus" type="button" onclick=' + insertcmd + '></button>\n';
	html += '</div>\n';
	
	$(function() {
		$('#' + form_id).append(html);	
	})
		
}