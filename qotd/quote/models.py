from django.db import models


class Quote(models.Model):
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    dateCreated = models.DateField()

    class Meta:
        db_table = 'quote'
