import imp
from django.http import JsonResponse
from django.template import context
from numpy import product
from demo.settings import RAZORPAY_API_SECRET_KEY, RAZORPAY_API_KEY
from django.shortcuts import render
from demo_app.models import ProductModel, ProductOrderListModel, ProductOrderModel
from demo_app.serializer import ProductSerializer
import razorpay
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def payment_home_page(request):
    # client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
    payment=client.order.create({'amount':50000,"currency":"INR","payment_capture":"1"})
    return render(request,'payment.html',{'order_id':payment['id'],"key":RAZORPAY_API_KEY})




def SaleView(request):
    context={}
    context['product']=ProductModel.objects.all()
    return render(request,'sale.html',context)


@api_view(['GET'])
def product_data(reqeust):
    product_id=reqeust.GET.get('product_id')
    data=ProductModel.objects.get(id=product_id)
    serializer = ProductSerializer(data, many=False)
    return JsonResponse(serializer.data)


@api_view(['POST'])
def Product_list_Post(request):
    product_id=request.POST['product_id']
    order_id=request.POST['order_id']
    qty=request.POST['qty']
    price=request.POST['price']
    total=request.POST['total']

    product=ProductModel.objects.get(id=product_id)
    order=ProductOrderModel.objects.get(id=order_id)
    p_qty=int(product.qty) - int(qty)
    ProductModel.objects.filter(id=product_id).update(qty=p_qty)
    ProductOrderListModel.objects.create(
        product_id =product,
        order_id=order,
        price=price,
        qty=qty,
        total = total
    )
    return JsonResponse({"data":"Success"})



