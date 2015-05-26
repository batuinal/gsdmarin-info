$(function() {

  var today = new Date();
  var hourNow = today.getHours();

  if (hourNow > 18) {
        $('.body').css('background-image', 'url(main/images/night.jpg)');
  
  }
  else if (hourNow > 12) {
        $('.body').css('background-image', 'url(main/images/lunch.jpg)');

  }
  else{
        $('.body').css('background-image', 'url(main/images/morning.jpg)');
  }
 });

/* FOR DEBUGGING
 var url = $('.body').css('background-image');
 //document.write('<div class="header2"> \n <div>' + oldurl + ' --> ' + newurl + '</div>\n</div>');
 IF YOU WANT TO USE URL
 $('.body').css('background-image', 'url(http://imgs.mi9.com/uploads/photography/4480/white-clouds-and-blue-sky_1600x1200_78556.jpg)');
 */