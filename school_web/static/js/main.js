$('document').ready(function() {
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true,

    });
    window.setInterval(function() { $('.carousel').carousel('next') }, 3000)
    $('.tabs').tabs();
    $(document).ready(function() {
        $('.sidenav').sidenav();
    });
    $(document).ready(function() {
        $('.collapsible').collapsible();
    });
});