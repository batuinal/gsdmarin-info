$(function() {

  var today = new Date();
  var hourNow = today.getHours();

  if (hourNow > 18) {
    document.write('<div class="header2"> \n <div>' + 'IF' + '</div>\n</div>');
    $('.body').css('background-image', 'url(http://imgs.mi9.com/uploads/photography/4480/white-clouds-and-blue-sky_1600x1200_78556.jpg)');
  } 
  else if (hourNow > 12) {
    document.write('<div class="header2"> \n <div>' + 'ELSEIF' + '</div>\n</div>');
    $('.body').css('background-image', 'url(http://www.naturewallpaper.eu/desktopwallpapers/sky/1366x768/after-sunset-sky-1366x768.jpg)');
  } 
  else{
    // Figure out how to give local links! //FIXME
    var oldurl = $('.body').css('background-image');
    $('.body').css('background-image', 'url(../images/index_BG.jpg');
	var newurl = $('.body').css('background-image');
    //document.write('<div class="header2"> \n <div>' + oldurl + ' --> ' + newurl + '</div>\n</div>');
  }
   
});
