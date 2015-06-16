var option_counter = 0;
function insert_option(form_id, values, texts) {
	
	if (values.length != texts.length) return;
	
	// Subfunction to convert variable into an injectable string.
	function vtos(val){	return "'" + val + "'";	}
	
	// Subfunction to convert array into an injectable string.
	function atos(array){
		retstr = "[";
		for (i = 0; i < array.length; i++) {
			if (i)
				retstr += ",";
			retstr += "'" + array[i] + "'";
		}
		retstr += "]";
		return retstr;
	}	
	
	newid = 'option_' + option_counter;
	selectname = 'select_' + option_counter;
	textboxname = 'textbox_' + option_counter;
	
	html = '<div id="' + newid + '">\n';
	html += '<select class="input-control select" name="' + selectname + '">\n';
	
	for (i = 0; i < values.length; i++){
		html += '<option value="' + values[i] + '"> ' + texts[i] + ' </option>\n';
	}
	
	insertcmd = '"insert_option(' + vtos(form_id) + ',' + atos(values) + ',' + atos(texts) + ')"';
	removecmd = "$(function(){&#36;('#" + newid + "').remove();})";
	
	html += '</select>\n';
	html += '<input class="input-control text" type="text" name=' + textboxname + '">\n';
	
	// First button is '+', next are '-'
	if (option_counter++)
		html += '<button class="button mif-minus" type="button" onclick=' + removecmd + '></button>\n';
	else
		html += '<button class="button mif-plus" type="button" onclick=' + insertcmd + '></button>\n';
	html += '</div>\n';
	
	$(function() {
		$('#' + form_id).append(html);	
	})
		
}