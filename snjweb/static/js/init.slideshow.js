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
    /*responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 1008,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 800,
          settings: "unslick"
        }

      ]*/
    });

    $('.front-slideshow').on('afterChange', function(event, slick, currentSlide){
      $('.slide-caption-layer').removeClass('animate-caption');
      $('.slick-active .slide-caption-layer').addClass('animate-caption');
    });
    $('.slick-active .slide-caption-layer').addClass('animate-caption');
});
