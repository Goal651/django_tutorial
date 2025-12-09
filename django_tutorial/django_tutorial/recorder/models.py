from django.db import models


# Create your models here.
class Record(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        db_table = "records"
