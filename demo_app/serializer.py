from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductOrderModel
        fields='__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductOrderListModel
        fields='__all__'