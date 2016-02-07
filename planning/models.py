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
        ordering = ('-date', )
        abstract = True


class HoppyUpdate(UpdateBase):
    image = ImageField(blank=True,
                       upload_to='hoppy_updates/')

    def get_absolute_url(self):
        return reverse('hoppy-detail',
                       args=[str(self.slug)])


class Announcement(UpdateBase):
    image = ImageField(blank=True,
                       upload_to='announcements/')

    def get_absolute_url(self):
        return reverse('announcement-detail',
                       args=[str(self.slug)])
