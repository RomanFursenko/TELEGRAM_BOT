from django.db import models

class Sa(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    categories = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)