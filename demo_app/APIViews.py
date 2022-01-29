from rest_framework.viewsets import ModelViewSet
from .serializer import *

class ProductAPIView(ModelViewSet):
    queryset=ProductModel.objects.all()
    serializer_class  = ProductSerializer


class OrderApiView(ModelViewSet):
    queryset=ProductOrderModel.objects.all()
    serializer_class =OrderSerializer


class OrderListApiView(ModelViewSet):
    queryset=ProductOrderListModel.objects.all()
    serializer_class =OrderListSerializer