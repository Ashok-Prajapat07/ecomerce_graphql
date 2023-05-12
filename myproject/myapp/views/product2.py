from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Product2(request):
    return render(request, 'product2.html')