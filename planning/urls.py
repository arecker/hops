from __future__ import unicode_literals

from django.conf.urls import url

from planning.views import MonthView, DayView, EventDetailView

urlpatterns = [url(r'^$', MonthView.as_view(), name='list'),
               url(r'^month/shift/$', MonthView.as_view(), name='month_shift'),
               url(r'^event-list/shift/$', MonthView.as_view(), name='event_list_shift'),
               url(r'^cal-and-list/shift/$', MonthView.as_view(), name='cal_and_list_shift'),
               url(r'^event/(?P<pk>[\w-]+)/$', EventDetailView.as_view(), name='detail'),
               url(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d{1})/$', MonthView.as_view(), name='list'),
               url(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d{1})/(?P<day>\d{2}|\d{1})/$', DayView.as_view(), name='day_list')]
