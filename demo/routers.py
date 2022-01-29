from rest_framework import routers
from demo_app.APIViews import *
router=routers.DefaultRouter()


router.register("product_api", ProductAPIView,basename="product_api")
router.register("customer_order",OrderApiView,basename="customer_order")
router.register("order_list",OrderListApiView,basename="order_list")