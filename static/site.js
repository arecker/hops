/*global $*/

function updateNavbar() {
    var activeLink = '#' + $('#activeLink').val();
    $('.navbar-nav').find('li').removeClass('active');
    $(activeLink).addClass('active');
}

function initBigImages() {
    $('.big-image').abigimage();
}

function initCalendar() {
    $.get('/api/events/', {}, function(d){
        $('#calendar').fullCalendar({
            header: {
                left: 'prev,next today',
                center: 'title'
            },
            editable: false,
            events: d,
            eventLimit: true
        });
    });

    $('#calPrev').click(function() {
        $('#calendar').fullCalendar('prev');
    });

    $('#calNext').click(function() {
        $('#calendar').fullCalendar('next');
    });

    $('#calToday').click(function() {
        $('#calendar').fullCalendar('today');
    });
}

$(document).ready(function() {
    updateNavbar();
    initBigImages();
    initCalendar();
});
