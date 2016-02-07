from django.views.generic import ListView
from happenings.views import (EventMonthView as EventMonthViewBase,
                              EventDayView as EventDayViewBase,
                              EventDetailView as EventDetailViewBase)

from models import HoppyUpdate


class MonthView(EventMonthViewBase):
    template_name = 'planning/month.html'


class DayView(EventDayViewBase):
    template_name = 'planning/day.html'


class EventDetailView(EventDetailViewBase):
    template_name = 'planning/event.html'


class HoppyUpdateListView(ListView):
    model = HoppyUpdate
