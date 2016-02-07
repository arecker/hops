from django.views.generic import ListView, DetailView
from happenings.views import (EventMonthView as EventMonthViewBase,
                              EventDayView as EventDayViewBase,
                              EventDetailView as EventDetailViewBase)

from models import HoppyUpdate, Announcement


class MonthView(EventMonthViewBase):
    template_name = 'planning/month.html'


class DayView(EventDayViewBase):
    template_name = 'planning/day.html'


class EventDetailView(EventDetailViewBase):
    template_name = 'planning/event.html'


class HoppyUpdateListView(ListView):
    model = HoppyUpdate
    paginate_by = 5


class HoppyUpdateDetailView(DetailView):
    model = HoppyUpdate


class AnnouncementListView(ListView):
    model = Announcement
    paginate_by = 5


class AnnouncementDetailView(DetailView):
    model = Announcement
