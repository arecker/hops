from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from hops import views
from hops.sitemap import SITEMAPS


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

               url(r'^thanks/$',
                   views.ThanksView.as_view(),
                   name='thanks'),

               url(r'^events/$',
                   views.CalendarView.as_view(),
                   name='events-list'),

               url(r'^events/(?P<slug>[^/]+)/$',
                   views.EventDetailView.as_view(),
                   name='event-detail'),

               url(r'^search/$', views.SearchView.as_view(), name='search'),

               url(r'^api/events/$', views.events, name='api-events'),

               url(r'^sitemap\.xml$', sitemap, {'sitemaps': SITEMAPS},
                   name='django.contrib.sitemaps.views.sitemap'),

               url(r'^robots\.txt$',
                   TemplateView.as_view(template_name='robots.txt',
                                        content_type='text/plain')),

               url(r'^$', views.HomeView.as_view(), name='home')]

# only active in development
# webserver will override this
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
