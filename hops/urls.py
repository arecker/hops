from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from hops import views


urlpatterns = [url(r'^admin/', admin.site.urls),

               url(r'^announcements/$',
                   views.AnnouncementListView.as_view(),
                   name='announcement-list'),
               url(r'^announcements/(?P<slug>[^/]+)/$',
                   views.AnnouncementDetailView.as_view(),
                   name='announcement-detail'),

               url(r'^gallery/$',
                   views.GalleryListView.as_view(),
                   name='gallery-list'),
               url(r'^gallery/(?P<slug>[^/]+)/$',
                   views.GalleryDetailView.as_view(),
                   name='gallery-detail'),


               url(r'^hoppy/$',
                   views.HoppyUpdateListView.as_view(),
                   name='hoppy-list'),
               url(r'^hoppy/(?P<slug>[^/]+)/$',
                   views.HoppyUpdateDetailView.as_view(),
                   name='hoppy-detail'),

               url(r'^newspaper/$',
                   views.NewspaperArchiveListView.as_view(),
                   name='newspaper-list'),

               url(r'^give/$',
                   views.GiveView.as_view(),
                   name='give'),

               url(r'^events/$',
                   views.CalendarView.as_view(),
                   name='events-list'),

               url(r'^events/(?P<slug>[^/]+)/$',
                   views.EventDetailView.as_view(),
                   name='event-detail'),

               url(r'^search/$', views.SearchView.as_view(), name='search'),

               url(r'^api/events/$', views.events, name='api-events'),

               url(r'^$', views.HomeView.as_view(), name='home')]

# only active in development
# webserver will override this
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
