from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

class Scope:

    PUBLIC = 0
    PRIVATE = 1

    SCOPE = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )

class Application(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    description = models.TextField()
    scope = models.IntegerField(choices=Scope.SCOPE, default=Scope.PRIVATE)
    application_file = models.FileField()
    app_link = models.URLField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.app_link = self.application_file.url
        super(Application, self).save(*args, **kwargs)
