$(window).scroll(function() {
    if($(this).scrollTop() >= 250) {
      // $('#top').fadeIn();
      $('#top').css({
       bottom : '20px'
      });
    }
    else {
     //  $('#top').fadeOut();
     $('#top').css({
       bottom : '-60px'
      });
    }
});

$('#top').click(function(e) {
   e.preventDefault()
   $('body,html').animate({
       scrollTop:0
   },1000);
});