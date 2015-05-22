$(function() {
  var today = new Date();
  var hourNow = today.getHours();
  //document.write('<div class="header2"> \n <div>' + 'hellow' + '</div>\n</div>');

  if (hourNow > 18) {

  $('.body').css('background-image', 'url("' + http://imgs.mi9.com/uploads/photography/4480/white-clouds-and-blue-sky_1600x1200_78556.jpg + '")');
  }
  else if (hourNow > 12) {
  $('.body').css('background-image', 'url("' + http://www.naturewallpaper.eu/desktopwallpapers/sky/1366x768/after-sunset-sky-1366x768.jpg + '")');
  }
  else{
  $('.body').css('background-image', 'url(images/index_BG.jpeg)');
  }
   
});
//url(images/index_BG.jpeg)