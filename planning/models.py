from uuid import uuid4

from django.db import models
from sorl.thumbnail import ImageField


class HoppyUpdate(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid4,
                          unique=True,
                          editable=False)

    date = models.DateField()
    title = models.CharField(max_length=120)
    # slug = models.SlugField()
    description = models.TextField(max_length=400, blank=True, null=True)
    image = ImageField(blank=True,
                       upload_to='hoppy_updates/')

    # def get_absolute_url(self):
    #     return reverse('hoppy-detail',
    #                    args=[str(self.slug)])

    def __unicode__(self):
        return self.description
