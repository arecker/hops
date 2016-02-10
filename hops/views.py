from django.views.generic import TemplateView, ListView, DetailView
from happenings.views import (EventMonthView as EventMonthViewBase,
                              EventDayView as EventDayViewBase,
                              EventDetailView as EventDetailViewBase)

from content.models import HoppyUpdate, Announcement


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        try:
            context['latest_hoppy'] = HoppyUpdate.objects.latest()
        except HoppyUpdate.DoesNotExist:
            context['latest_hoppy'] = None

        try:
            context['latest_announcement'] = Announcement.objects.latest()
        except Announcement.DoesNotExist:
            context['latest_announcement'] = None

        return context


class MonthView(EventMonthViewBase):
    template_name = 'month.html'


class DayView(EventDayViewBase):
    template_name = 'day.html'


class EventDetailView(EventDetailViewBase):
    template_name = 'event.html'


class HoppyUpdateListView(ListView):
    model = HoppyUpdate
    template_name = 'hoppyupdate_list.html'
    paginate_by = 5


class HoppyUpdateDetailView(DetailView):
    model = HoppyUpdate
    template_name = 'hoppyupdate_detail.html'


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement_list.html'
    paginate_by = 5


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcement_detail.html'