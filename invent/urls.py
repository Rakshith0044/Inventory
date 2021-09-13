"""invent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from trial.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register',register,name='login'),
    path('login',login,name='login'),
    path('admins',admins,name='admins'),
    path('purchase',purchase,name='purchase'),
    path('index',index,name='logout'),
    path('supplier',supplier,name='supplier'),
    path('addsup',addsup,name='addsup'),
    path('sell',sell,name='sell'),
]
