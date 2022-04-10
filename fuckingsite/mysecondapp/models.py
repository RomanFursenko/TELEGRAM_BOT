from django.db import models

class Sa(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
