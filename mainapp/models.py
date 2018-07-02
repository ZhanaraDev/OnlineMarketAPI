from django.db import models

# Create your models here.

class Product(models.Model):
    class Meta:
        unique_together = (('name','universal_product_code'))
    name = models.CharField(max_length=250)
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    universal_product_code = models.CharField(max_length=250)