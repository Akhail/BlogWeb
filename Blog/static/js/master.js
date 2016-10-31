$(window).bind('scroll', function () {
    if ($(window).scrollTop() > 27) {
        $('.hide-menu').addClass('show');
    } else {
        $('.hide-menu').removeClass('show');
    }
});
