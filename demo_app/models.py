from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from statistics import mode
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from numpy import product
# Create your models here.

class ProductModel(models.Model):
    product_name=models.CharField(max_length=30,null=True,blank=True)
    price=models.IntegerField()
    qty=models.IntegerField()
    p_img=models.ImageField(null=True,blank=True)
    user=models.OneToOneField(User,null=True, blank=True,on_delete=CASCADE)

    class Meta:
        db_table="product_table"
        

class ProductOrderModel(models.Model):
    cust_name=models.CharField(max_length=30)
    grand_total=models.IntegerField()
    user=models.OneToOneField(User,null=True,blank=True,on_delete=CASCADE)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        db_table="order_table"

class ProductOrderListModel(models.Model):
    product_id=models.ForeignKey(ProductModel,null=True,blank=True,on_delete=CASCADE)
    order_id=models.ForeignKey(ProductOrderModel,null=True,blank=True,on_delete=CASCADE)
    qty=models.IntegerField()
    price=models.IntegerField()
    total=models.IntegerField()

    class Meta:
        db_table="order_list_table"

