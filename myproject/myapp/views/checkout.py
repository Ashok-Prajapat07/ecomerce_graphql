from django.shortcuts import render


# Create your views here.
def Checkout(request):
    return render(request, 'checkout.html')