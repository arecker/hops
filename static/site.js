/*global $*/

function updateNavbar() {
    var activeLink = '#' + $('#activeLink').val();
    $('.navbar-nav').find('li').removeClass('active');
    $(activeLink).addClass('active');
}

$(document).ready(function() {
    updateNavbar();
});
