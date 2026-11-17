from django.db import models


class Comic(models.Model):
    title = models.CharField(max_length=67)
    description = models.TextField(blank=True)
    editorial = models.CharField(max_length=67, blank=True)

    class Meta:
        db_table = "comic"
        app_label = "hello_api"