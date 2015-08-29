function scaf_begin_init(page){
	$.ready(function() {
		$("#mainheading").html(page + " Page");
	});
}

function init(page){
	scaf_begin_init(page);
}