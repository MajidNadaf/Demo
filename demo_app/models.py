from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class ProductModel(models.Model):
    product_name=models.CharField(max_length=30,null=True,blank=True)
    price=models.IntegerField()
    p_img=models.ImageField(null=True,blank=True)
    user=models.OneToOneField(User,null=True, blank=True,on_delete=CASCADE)

    class Meta:
        db_table="product"
        