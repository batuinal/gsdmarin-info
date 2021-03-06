displayTime('localtime','isttime');

function displayTime(local_id, ist_id, show_colon){
    
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

	var date = new Date();
	
	var h_local = padTime(date.getHours());
	var m_local = padTime(date.getMinutes());
	var s_local = padTime(date.getSeconds());
	
	var utc = date.getTime() + (date.getTimezoneOffset() * 60*1000);
	
	var newdate;
	if (ist_DST()){
		newdate = new Date(utc + (3*60*60*1000));
	}
	else{
		newdate = new Date(utc + (2*60*60*1000))
	}
	
	var h_ist = padTime(newdate.getHours());
	var m_ist = padTime(newdate.getMinutes());
	
	if (show_colon) {
		document.getElementById(local_id).innerHTML = h_local + ':' + m_local;
		document.getElementById(ist_id).innerHTML = h_ist + ':' + m_ist;
		setTimeout(displayTime,500,local_id,ist_id,0);
	else {
		document.getElementById(local_id).innerHTML = h_local + ' ' + m_local;
		document.getElementById(ist_id).innerHTML = h_ist + ' ' + m_ist;
		setTimeout(displayTime,500,local_id,ist_id,1);
	}
	
	return true;
}