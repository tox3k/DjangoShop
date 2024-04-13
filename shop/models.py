from django.db import models

class Developer(models.Model):
    id = models.IntegerField(verbose_name='Developer', primary_key=True)
    name = models.TextField(max_length=255, null=False, unique=True)


class Product(models.Model):
    id = models.IntegerField(verbose_name='Id', primary_key=True)
    name = models.TextField(null=False, max_length=255, unique=True)
    slug = models.SlugField(max_length=15, null=False)
    description = models.TextField(verbose_name='Description', max_length=255)
    developer = models.ForeignKey('Developer',to_field='name', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Price', null=False, decimal_places=2, max_digits=15)
    count = models.IntegerField(verbose_name='Count', null=False)



