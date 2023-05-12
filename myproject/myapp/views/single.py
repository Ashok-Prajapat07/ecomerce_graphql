from django.shortcuts import render
# Create your views here.

def Single(request):
    return render(request, 'single.html')