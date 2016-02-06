from happenings.views import (EventMonthView as EventMonthViewBase,
                              EventDayView as EventDayViewBase,
                              EventDetailView as EventDetailViewBase)


class MonthView(EventMonthViewBase):
    template_name = 'planning/month.html'


class DayView(EventDayViewBase):
    template_name = 'planning/day.html'


class EventDetailView(EventDetailViewBase):
    template_name = 'planning/event.html'
