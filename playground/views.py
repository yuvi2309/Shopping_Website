from genericpath import exists
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem
from store.models import OrderItem


# Create your views here.
# request -> responce (takes request and return responce)
# request handler
 
def say_hello(request):
    #pull data from db
    #transform 
    #send email
    # print(query_set)
    # query_set = Product.objects.
    # query_set = OrderItem.objects.values('product_id')

    return render(request, 'hello.html',{'name':'Yuvraj'})
