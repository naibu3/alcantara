from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=255, null=False, primary_key=True)
    comment = models.TextField(max_length=1000, null=True)
    uds = models.IntegerField(default=0)
    place = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name