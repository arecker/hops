from uuid import uuid4

from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField


class UpdateBase(models.Model):
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
        return self.description

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


class BannerAdvertisementQuerySet(models.QuerySet):
    def pluck(self):
        try:
            return self.order_by('?').first()
        except self.model.DoesNotExist:
            return None


class BannerAdvertisement(models.Model):
    objects = BannerAdvertisementQuerySet.as_manager()

    image = ImageField(upload_to='banner_ads')
    link = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.image.file.name

    class Meta:
        verbose_name = 'Banner Ad'
        verbose_name_plural = 'Banner Ads'
