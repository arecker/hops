from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from hops.views import HomeView
from planning.views import HoppyUpdateListView, HoppyUpdateDetailView

urlpatterns = [url(r'^admin/', admin.site.urls),

               url(r'^calendar/',
                   include('planning.urls',
                           namespace='calendar')),

               url(r'^hoppy/$',
                   HoppyUpdateListView.as_view(),
                   name='hoppy-list'),
               url(r'^hoppy/(?P<slug>[^/]+)/$',
                   HoppyUpdateDetailView.as_view(),
                   name='hoppy-detail'),

               url(r'^$', HomeView.as_view(), name='home')]

# only active in development
# webserver will override this
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
