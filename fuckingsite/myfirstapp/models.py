from django.db import models

class Fa(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    # published = models.DateField(null=True, blank=True)

