"""AuthenticationSystemAjax URL Configuration

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
from app.views import logoutFun,home,main,signup_ajax_function,signin_ajax_function

urlpatterns = [
   path('admin/', admin.site.urls),
   path('reg/',signup_ajax_function,name='reg'),
    path('login/',signin_ajax_function,name='login'),
    path('',main,name='main'),
    path('home/',home,name='home'),
     path('logout/',logoutFun,name='logout'),
]
