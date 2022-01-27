from rest_framework.viewsets import ModelViewSet
from .serializer import *

class ProductAPIView(ModelViewSet):
    queryset=ProductModel.objects.all()
    serializer_class  = ProductSerializer