from django.shortcuts import render



# Create your views here.
def Payment(request):
    return render(request, 'payment.html')