from uuid import uuid4

from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone
from sorl.thumbnail import ImageField


def search(term):
    results = {}

    for k, m in [('announcements', Announcement),
                 ('hoppies', HoppyUpdate),
                 ('galleries', Gallery)]:
        results[k] = m.objects.filter_by_searchable_fields(term)

    return results


class UpdateBaseQueryset(models.QuerySet):
    def filter_by_searchable_fields(self, term):
        return self.filter(Q(title__contains=term) |
                           Q(description__contains=term))


class UpdateBase(models.Model):
    objects = UpdateBaseQueryset.as_manager()

    id = models.UUIDField(primary_key=True,
                          default=uuid4,
                          unique=True,
                          editable=False)

    date = models.DateField()
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    @property
    def body_teaser(self):
        '''return a truncated body'''
        words = self.body.split()[:50]
        return ' '.join(words) + '...'

    class Meta:
        abstract = True


class HoppyUpdate(UpdateBase):
    image = ImageField(blank=True,
                       upload_to='hoppy_updates/')

    def get_absolute_url(self):
        return reverse('hoppy-detail',
                       args=[str(self.slug)])

    class Meta:
        verbose_name_plural = 'Hoppy Updates'
        ordering = ('-date', )
        get_latest_by = 'date'


class Announcement(UpdateBase):
    image = ImageField(blank=True,
                       upload_to='announcements/')

    def get_absolute_url(self):
        return reverse('announcement-detail',
                       args=[str(self.slug)])

    class Meta:
        ordering = ('-date', )
        get_latest_by = 'date'


class Gallery(UpdateBase):
    image = ImageField(blank=True,
                       upload_to='gallery_covers',
                       verbose_name='Cover Image')

    def get_absolute_url(self):
        return reverse('gallery-detail',
                       args=[str(self.slug)])

    class Meta:
        verbose_name_plural = 'Galleries'
        ordering = ('-date', )
        get_latest_by = 'date'


class GalleryImage(models.Model):
    image = ImageField(upload_to='gallery_images')
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return self.image.file.name


class PartnerQuerySet(models.QuerySet):
    def pluck(self):
        try:
            return self.filter(in_ads=True).order_by('?').first()
        except self.model.DoesNotExist:
            return None

    def credits(self):
        return self.filter(in_credits=True)


class Partner(models.Model):
    objects = PartnerQuerySet.as_manager()

    name = models.CharField(max_length=120, blank=True, null=True)
    image = ImageField(upload_to='banner_ads', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    in_credits = models.BooleanField(default=False, verbose_name='include in credits')
    in_ads = models.BooleanField(default=False, verbose_name='include in banner ads')

    def clean(self):
        if not self.image and self.in_ads:
            raise ValidationError('needs an image to be included in banner ads')
        if not self.name and self.in_credits:
            raise ValidationError('needs name to be included in credits')

    def __unicode__(self):
        return self.name or '(no name)'


class NewspaperArchive(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='newspapers')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Newspaper Archive'
        ordering = ('-date', )


class EventQuerySet(models.QuerySet):
    def upcoming(self):
        today = timezone.now()
        next_week = today + timezone.timedelta(weeks=1)
        return self.filter(start__gte=today,
                           start__lte=next_week)


class Event(models.Model):
    objects = EventQuerySet.as_manager()

    id = models.UUIDField(primary_key=True,
                          unique=True,
                          default=uuid4,
                          editable=False)

    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = ImageField(upload_to='events/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def clean(self):
        if self.end and self.start > self.end:
            raise ValidationError('Start cannot fall after end')

    def get_absolute_url(self):
        return reverse('event-detail',
                       args=[str(self.slug)])

    def __unicode__(self):
        return self.title
