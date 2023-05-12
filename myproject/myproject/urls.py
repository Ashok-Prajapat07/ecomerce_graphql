"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views.index import Index
from myapp.views.about import About
from myapp.views.checkout import Checkout
from myapp.views.contact import Contact
from myapp.views.help import Help
from myapp.views.payment import Payment
from myapp.views.privacy import Privacy
from myapp.views.product import Product
from myapp.views.product2 import Product2
from myapp.views.single import Single
from myapp.views.single2 import Single2
from myapp.views.terms import Terms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('about/', About, name='about'),
    path('checkout/', Checkout, name='checkout'),
    path('contact', Contact, name='contact'),
    path('help', Help, name='help'),
    path('payment', Payment, name='payment'),
    path('privacy', Privacy, name='privacy'),
    path('product', Product, name='product'),
    path('product2', Product2, name='product2'),
    path('single', Single, name='single'),
    path('single2', Single2, name='sin2gle'),
    path('terms', Terms, name='terms'),
]
