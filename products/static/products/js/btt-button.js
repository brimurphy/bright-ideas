$(window).scroll(function() {
    let backUpButton = $(this).scrollTop();
    if (backUpButton > 500) {
        $(".btt-btn").fadeIn();
    } else {
        $(".btt-btn").fadeOut();
    }
})

$("#btt").click(function() {
    window.scrollTo(0,0)
})