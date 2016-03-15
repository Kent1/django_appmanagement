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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Application, self).save(*args, **kwargs)
