$(document).ready(function () {

    var menu = $('.navbar-nav');
    var origOffsetY = menu.offset().top;

    function scroll() {
        if ($(window).scrollTop() >= origOffsetY) {
           $('.navbar').removeClass('navbar-static-top');
           $('.navbar').addClass('navbar-fixed-top');
           $('.content').addClass('menu-padding');
        } else {
          $('.navbar').removeClass('navbar-fixed-top');
          $('.navbar').addClass('navbar-static-top');
          $('.content').removeClass('menu-padding');
          origOffsetY = menu.offset().top;
        }


    }

    document.onscroll = scroll;

});