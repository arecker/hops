from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from hops import views


urlpatterns = [url(r'^admin/', admin.site.urls),

               url(r'^calendar/',
                   include('hops.calendar_urls', namespace='calendar')),

               url(r'^announcements/$',
                   views.AnnouncementListView.as_view(),
                   name='announcement-list'),
               url(r'^announcements/(?P<slug>[^/]+)/$',
                   views.AnnouncementDetailView.as_view(),
                   name='announcement-detail'),


               url(r'^hoppy/$',
                   views.HoppyUpdateListView.as_view(),
                   name='hoppy-list'),
               url(r'^hoppy/(?P<slug>[^/]+)/$',
                   views.HoppyUpdateDetailView.as_view(),
                   name='hoppy-detail'),

               url(r'^$', views.HomeView.as_view(), name='home')]

# only active in development
# webserver will override this
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
