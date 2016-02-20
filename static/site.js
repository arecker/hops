/*global $*/

function updateNavbar() {
    var activeLink = '#' + $('#activeLink').val();
    $('.navbar-nav').find('li').removeClass('active');
    $(activeLink).addClass('active');
}

function initBigImages() {
    $('.big-image').abigimage();
}

$(document).ready(function() {
    updateNavbar();
    initBigImages();
});
