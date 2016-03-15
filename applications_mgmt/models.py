from __future__ import unicode_literals

from django.db import models

class Scope:

    PUBLIC = 0
    PRIVATE = 1

    SCOPE = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )

class Application(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    scope = models.IntegerField(choices=Scope.SCOPE, default=Scope.PRIVATE)
    application_file = models.FileField()
