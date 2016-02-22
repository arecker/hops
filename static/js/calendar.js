/*global $*/
(function() {
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
    });
}());
