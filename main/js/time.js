function displayTime(id){

var today = new Date();
var dateNow = today.toDateString();
var timeNow = today.toTimeString();

document.getElementById(id).innerHTML = timeNow;
setTimeout('displayTime("' + id + '");','1000');
}