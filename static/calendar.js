/*global $*/
$(document).ready(function() {
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
});
