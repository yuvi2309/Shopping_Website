from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> responce (takes request and return responce)
# request handler

def calculate():
    x = 1
    y = 2
    return x
    
def say_hello(request):
    #pull data from db
    #transform 
    #send email
    x=calculate()
    return render(request, 'hello.html',{'name':'Yuvraj'})
