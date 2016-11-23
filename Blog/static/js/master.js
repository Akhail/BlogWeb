$(window).bind('scroll', function () {
    if ($(window).scrollTop() > 27) {
        $('.hide-menu').addClass('show');
    } else {
        $('.hide-menu').removeClass('show');
    }
});

// $('#search').on('click', function () {
//     $('#search-text').toggleClass('visible-input');
// });
//
// $('#search-text').keydown(function (event) {
//     if (event.keyCode == 13) {
//         this.form.submit();
//         return false;
//     }
// });