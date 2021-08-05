from django.db import models
from django.db.models import Model, CharField, PositiveIntegerField, TextField


# Create your models here.

class Item(Model):
    name = CharField(max_length=100)
    brand = CharField(max_length=50, default="")
    quantity = PositiveIntegerField()
    description = TextField(default="")

    def __repr__(self):
        return f'Item: {self.name}'

    def __str__(self):
        return f'Item: {self.name} q:{self.quantity}'
