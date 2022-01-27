from demo.settings import RAZORPAY_API_SECRET_KEY, RAZORPAY_API_KEY
from django.shortcuts import render
import razorpay

# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def payment_home_page(request):
    # client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
    payment=client.order.create({'amount':50000,"currency":"INR","payment_capture":"1"})
    return render(request,'payment.html',{'order_id':payment['id'],"key":RAZORPAY_API_KEY})

