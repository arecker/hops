from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from content import models


class ViewSitemap(Sitemap):
    def items(self):
        return ['home', 'give']

    def location(self, item):
        return reverse(item)


class BaseSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return self.model.objects.all()

    def lastmod(self, obj):
        return obj.date


class AnnouncementSitemap(BaseSitemap):
    model = models.Announcement


class GallerySitemap(BaseSitemap):
    model = models.Gallery


class HoppySitemap(BaseSitemap):
    model = models.HoppyUpdate


class EventSitemap(BaseSitemap):
    model = models.Event

    def lastmod(self, obj):
        return obj.start


SITEMAPS = {'views': ViewSitemap,
            'announcements': AnnouncementSitemap,
            'galleries': GallerySitemap,
            'hoppies': HoppySitemap,
            'events': EventSitemap}
