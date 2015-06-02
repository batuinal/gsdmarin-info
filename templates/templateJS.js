var today = new Date();
var time = today.getHours();
var greeting;

if (time > 18) {
    greeting = 'Good Evening'
    //*$('ul').css('background-image', 'http://ginva.com/wp-content/uploads/2012/07/city-skyline-wallpapers-006.jpg');
     
}
else if (time > 12){
    greeting = 'Good Afternoon'
}

else{
        greeting = 'Good Morning'
        //$('ul').css('background-image', 'http://ginva.com/wp-content/uploads/2012/07/city-skyline-wallpapers-009.jpg');
}

document.write('<h1>' + greeting + '</h1>')

http://www.edcint.co.nz/misc/autologin/