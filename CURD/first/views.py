from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request,'home.html')

def add(request):

    num1 = request.GET['num1']
    num2 = request.GET['num2']
    result = int(num1) + int(num2)
    return render(request,'result.html',{'result' : result})
    

# Create your views here.
