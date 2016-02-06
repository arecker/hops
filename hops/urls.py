from django.conf.urls import url, include
from django.contrib import admin

from hops.views import HomeView

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^calendar/',
                   include('happenings.urls',
                           namespace='calendar')),
               url(r'^$', HomeView.as_view(), name='home')]
