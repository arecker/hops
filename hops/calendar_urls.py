from django.conf.urls import url

from hops import views


"""Overrides for happenings plugin

TODO: Not sure we need all of these.
"""


urlpatterns = [url(r'^$',
                   views.MonthView.as_view(),
                   name='list'),

               url(r'^month/shift/$',
                   views.MonthView.as_view(),
                   name='month_shift'),

               url(r'^event-list/shift/$',
                   views.MonthView.as_view(),
                   name='event_list_shift'),

               url(r'^cal-and-list/shift/$',
                   views.MonthView.as_view(),
                   name='cal_and_list_shift'),

               url(r'^event/(?P<pk>[\w-]+)/$',
                   views.EventDetailView.as_view(),
                   name='detail'),

               url(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d{1})/$',
                   views.MonthView.as_view(),
                   name='list'),

               url(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d{1})/(?P<day>\d{2}|\d{1})/$',
                   views.DayView.as_view(),
                   name='day_list')]
