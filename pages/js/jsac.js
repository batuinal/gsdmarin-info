classes = ['text', 'num', 'bool', 'char', 'ship', 'date', 'time', 'link', 'loc', 'coord', 'file'];

$(function() {
	
	function jsac_apply_text(elts){}
	
	function jsac_apply_num(elts){}
	
	function jsac_apply_bool(elts){
		for (var i = 0; i < elts.length; i++) {
			if (elts[i].innerHTML == "Yes")
				elts[i].style.backgroundColor = "#00ff00";
			else if (elts[i].innerHTML == "No")
				elts[i].style.backgroundColor = "#ffff00";
			else
				elts[i].style.backgroundColor = "#ffffff";
		}
	}
	
	function jsac_apply_char(elts){
		for (var i = 0; i < elts.length; i++) {
			if (elts[i].innerHTML == "a" || elts[i].innerHTML == "A")
				elts[i].style.backgroundColor = "#ff0000";
			else if (elts[i].innerHTML == "b" || elts[i].innerHTML == "B")
				elts[i].style.backgroundColor = "#ff7f00";
			else if (elts[i].innerHTML == "c" || elts[i].innerHTML == "C")
				elts[i].style.backgroundColor = "#ffff00";
			else
				elts[i].style.backgroundColor = "#ffffff";	
		}
	}
	
	function jsac_apply_ship(elts){

	}
	
	function jsac_apply_date(elts){

	}
	
	function jsac_apply_time(elts){

	}
	
	function jsac_apply_link(elts){

	}
	
	function jsac_apply_loc(elts){

	}
	
	function jsac_apply_coord(elts){

	}
	
	function jsac_apply_file(elts){

	}
	
	for (var i = 0; i < classes.length; i++) {
		jsac = classes[i];
		elts = $(".jsac_" + classes[i]);
		
		if (jsac == 'text')
			jsac_apply_text(elts);
		else if (jsac == 'num')
			jsac_apply_num(elts);
		else if (jsac == 'bool')
			jsac_apply_bool(elts);
		else if (jsac == 'char')
			jsac_apply_char(elts);
		else if (jsac == 'ship')
			jsac_apply_ship(elts);
		else if (jsac == 'date')
			jsac_apply_date(elts);
		else if (jsac == 'time')
			jsac_apply_time(elts);
		else if (jsac == 'link')
			jsac_apply_link(elts);
		else if (jsac == 'loc')
			jsac_apply_loc(elts);
		else if (jsac == 'coord')
			jsac_apply_coord(elts);
		else if (jsac == 'file')
			jsac_apply_file(elts);
		else 
			throw "jsac_error";	
	}
});