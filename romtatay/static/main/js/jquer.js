var owl = $('.owl-carousel');
owl.owlCarousel({
    items: 9,
    loop: true,
    margin: 10,
    autoplay: true,
    autoplaySpeed: 10000,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 2
        },
        800: {
            items: 5
        },
        1000: {
            items: 8
        }
    }
});
$('.play').on('click', function() {
    owl.trigger('play.owl.autoplay', [1000])
})
$('.stop').on('click', function() {
    owl.trigger('stop.owl.autoplay')
})