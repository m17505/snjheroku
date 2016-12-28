$(document).ready(function () {
    $('.front-slideshow').slick({
    dots: false,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 8000,
    speed: 800,
    mobileFirst: false,
    nextArrow: '<i class="fa fa-angle-right"></i>',
    prevArrow: '<i class="fa fa-angle-left"></i>',
    slide: '.frontslide',
    });

    $('.front-slideshow').on('afterChange', function(event, slick, currentSlide){
      $('.slide-caption-layer').removeClass('animate-caption');
      $('.slick-active .slide-caption-layer').addClass('animate-caption');
    });
    $('.slick-active .slide-caption-layer').addClass('animate-caption');
});
