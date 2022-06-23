from operator import mod
from statistics import mode
import uuid
from django.db import models
from uuid import uuid4

# Create your models here.
class Prompt(models.Model):
    VALUE_TYPE = (
        ('New Instruct Davinci', 'New-davinci'),
        ('Instruct Davinci', 'Old-davinci'),
        ('Instruct Curie', 'Curie')
    )
    name = models.CharField(max_length=200)
    prompt = models.TextField(blank=True, null=True)
    engine = models.CharField(max_length=25, blank=True, null=True, choices=VALUE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self) -> str:
        return self.name
