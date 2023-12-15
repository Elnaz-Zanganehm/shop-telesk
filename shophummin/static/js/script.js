$(function() {
    $(window).scroll(function(){
         if($(this).scrollTop() > 50) {
            $('#main-menu').addClass('scroll')
         }
    })

    const myCollapsible = document.getElementById('#main-menu')
        myCollapsible.addEventListener('show.bs.collapse', () => {
            $('#main-menu').addClass('.scroll-m');   
  // do something...
})

        myCollapsible.addEventListener('hidden.bs.collapse', () => {
            $('#main-menu').removeClass('.scroll-m');   
  // do something...
})


})