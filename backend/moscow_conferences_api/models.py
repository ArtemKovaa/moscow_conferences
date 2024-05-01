from django.db import models


class Location(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, unique=True, blank=False)


class Conference(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=50, unique=True, blank=False)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField(blank=False)
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        blank=False
    )
