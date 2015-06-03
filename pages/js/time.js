displayTime('#localdate', '#istdate', '#localtime','#isttime',1);

function displayTime(ldate_id, idate_id, ltime_id, itime_id, show_colon){
    
	function ist_DST(){
	var today = new Date;
	var yr = today.getFullYear();
	var dst_start = new Date("March 31, "+yr+" 03:00:00"); // 2nd Sunday in March can't occur after the 14th
	var dst_end = new Date("October 31, "+yr+" 04:00:00"); // 1st Sunday in November can't occur after the 7th
	var day = dst_start.getDay(); // day of week of 14th
	dst_start.setDate(31-day); // Calculate Last Sunday in March of this year
	day = dst_end.getDay(); // day of the week of 7th
	dst_end.setDate(31-day); // Calculate first Sunday in October of this year
	if (today >= dst_start && today < dst_end){ //does today fall inside of DST period?
		return true; //if so then return true
	}
	return false; //if not then return false
}

	function padTime(n) {
	return (n < 10) ? '0' + n : n;
    }

	var localdate = new Date();
	
	var Y_local = localdate.getFullYear();
	var M_local = localdate.getMonth() + 1;
	var D_local = localdate.getDay();
	var h_local = padTime(localdate.getHours());
	var m_local = padTime(localdate.getMinutes());
	
	var utc = localdate.getTime() + (localdate.getTimezoneOffset() * 60*1000);
	
	var istdate;
	if (ist_DST()){
		istdate = new Date(utc + (3*60*60*1000));
	}
	else{
		istdate = new Date(utc + (2*60*60*1000))
	}
	
	var Y_ist = istdate.getFullYear();
	var M_ist = istdate.getMonth() + 1;
	var D_ist = istdate.getDay();
	var h_ist = padTime(istdate.getHours());
	var m_ist = padTime(istdate.getMinutes());
	
	$(function(){
		$(ldate_id).text(M_local + '/' + D_local + '/' + Y_local);
		$(idate_id).text(M_ist + '/' + D_ist + '/' + Y_ist);
	});
	
	if (show_colon == 1) {
		$(function(){ 		
			$(ltime_id).text(h_local + ':' + m_local); 
			$(itime_id).text(h_ist + ':' + m_ist);
		});
		setTimeout(displayTime,500,ldate_id,idate_id,ltime_id,itime_id,0);
	}
	else {
		$(function(){
			$(ltime_id).text(h_local + ' ' + m_local); 			
			$(itime_id).text(h_ist + ' ' + m_ist); 
		});
		setTimeout(displayTime,500,ldate_id,idate_id,ltime_id,itime_id,1);
	}
	
	return true;
}