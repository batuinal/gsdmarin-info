classes = ['text', 'num', 'bool', 'char', 'ship', 'date', 'time', 'link', 'loc', 'coord', 'file'];

$(function() {
	
	function jsac_apply_text(elts){}
	
	function jsac_apply_num(elts){}
	
	function jsac_apply_bool(elts){
		elts.each( function() {
			text = $(this).html().toUpperCase();
			css = "#ffffff";
			if ($(this).html() == "Y")
				css = "#00ff00";
			else if ($(this).html() == "N")
				css = "#ffff00";

			$(this).css("background-color", css);
		});
	}
	
	function jsac_apply_char(elts){
		elts.each( function() {
			text = $(this).html().toUpperCase();
			css = "#ffffff";
			if (text == "A")
				css = "#ff0000";
			else if (text == "B")
				css = "#ff4500";
			else if (text == "C")
				css = "#ffff00";
			
			$(this).css("background-color", css);
		});
	}
	
	function jsac_apply_ship(elts){
		elts.each( function() {
			var text = $(this).html().toUpperCase();
			var css = "#ffffff";
			if (text == "CANO")
				css = "#ff4500";
			else if (text == "DODO")
				css = "#00ffff";
			else if (text == "HAKO")
				css = "#7fff00";
			else if (text == "ZEYNO")
				css = "#ffd700";
			
			$(this).css("background-color", css);
		});
	}
	
	//The date format should be YY/MM/DD	
	function jsac_apply_date(elts){
		for (var i = 0; i <elts.length; i++){
			var cur = elts[i].innerHTML;
			/*
			if (cur.length != 8){ alert("Please check the Dates Entered"); break;}
			if ((cur[2] && cur[5]) != "/") { alert("Please check the Dates Entered"); break;}
			for (var j = 0; j < elts.length; j++){
				if (j == 2 || j == 5) continue;
				if (isNaN(cur[j])) { alert("Please check the Dates Entered"); break;}
			}
			*/
		}
	}
	
	//Same as above not implemented
	function jsac_apply_time(elts){
		for (var i = 0; i <elts.length; i++){
			var cur = elts[i].innerHTML;
			
			/*
			if (cur == "0:00:00" or !cur.length){
				var timeNow = new Date();
		  		var hours   = timeNow.getHours();
		 		var minutes = timeNow.getMinutes();
		  		var seconds = timeNow.getSeconds();
		  		var timeString = "" + hours;
  				timeString  += ((minutes < 10) ? ":0" : ":") + minutes;
  				timeString  += ((seconds < 10) ? ":0" : ":") + seconds;
		  		elts[i].innerHTML = timeString;
		  	}
			*/
		 }
		 
	}
	

	function jsac_apply_link(elts){
		elts.each(function() {
			var html = $(this).html;
			var corr = "http"
			var i = 0;
			for (; i < 4; i++){
				if (corr[i] != html[i])	{ break;}
			}
			var new_html = html;
			if (i != 4)
				new_html = "https://" + new_html;
			
			$(this).html(new_html);
		});
	}
	
	function jsac_apply_loc(elts){
		elts.each( function() {
			$(this).click("request('POST','https://www.google.com/maps',['q']," + $(this).html() + ");");
		});
	}
	
	function jsac_apply_coord(elts){
		elts.each( function() {
			$(this).click("request('POST','https://www.google.com/maps',['q']," + $(this).html() + ");");
		});
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