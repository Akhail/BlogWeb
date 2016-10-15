var num = 40; //number of pixels before modifying styles

$(window).bind('scroll', function () {
    if ($(window).scrollTop() > num) {
        $('.hide-menu').addClass('show');
    } else {
        $('.hide-menu').removeClass('show');
    }
});
