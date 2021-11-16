from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.TextField(default="hello", null=True)
    timestamp = models.FloatField(default=-1.0, null=True)

from mongoengine import Document, fields

# Create your models here.
class TestDocument(Document):
    name = fields.StringField(default="hello", null=True)
    timestamp = fields.FloatField(default=-1.0, null=True)