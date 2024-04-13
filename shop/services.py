from .models import Product, Developer
from django.db import models
def add_model(model, **kwargs):
    model(**kwargs).save()