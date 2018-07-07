from django.db import models
import uuid

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=64)
    checked = models.BooleanField()

    # class Meta:
    #     verbose_name = 'task model'
    #     verbose_name_plural = 'task model'
    #     unique_together=['text', 'checked']