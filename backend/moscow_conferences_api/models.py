import uuid
from django.db import models


class Conference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField(blank=False)
    location = models.CharField(max_length=100, blank=False)
