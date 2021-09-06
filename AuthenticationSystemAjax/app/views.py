from django.contrib.auth import authenticate, forms, login, logout
from django.shortcuts import render
from .forms import UserCreationForm,LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User


# Create your views here.
def signup_ajax_function(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        fname = request.POST.get('first_name')

        if form.is_valid():
            if User.objects.filter(email=email).exists():
               return JsonResponse({"error_email":"Email already exists"}) 
            else:
                form.save()
                return JsonResponse({"status":200})      
        else:
            error_name =[]
            error_value = []
            for i,j in form.errors.as_data().items():
                print(i,j[0])
                for m in j[0]:
                    error_value.append(m)
                error_name.append(i)
                
            print(form.errors.as_data())
            error = form.errors.as_data()
            return JsonResponse({"status":"errors","error_name":error_name,"error_value":error_value})
    else:
        return JsonResponse({"status":"Failed"})



def signin_ajax_function(request):
    if request.method == 'POST':
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            try:
                usr = authenticate(username=username,password = pas)
            except:
                return JsonResponse({'status':203})
            login(request,usr)
            return JsonResponse({'status':200})     
            
        else:
            error_name =[]
            error_value = []
            for i,j in form.errors.as_data().items():
                print(i,j[0])
                for m in j[0]:
                    error_value.append(m)
                error_name.append(i)
                
            print(form.errors.as_data())
            error = form.errors.as_data()
            return JsonResponse({"status":"errors","error_name":error_name,"error_value":error_value})
    else:
        return JsonResponse({"status":"Failed"})



def main(reqest):
    userCreation = UserCreationForm()
    loginForm = LoginForm()
    return render(reqest,'login.html',{'userCreation':userCreation,'loginForm':loginForm})
    

def home(reqest):
    if reqest.user.is_authenticated:
        return render(reqest,'home.html')
    else:
        return HttpResponseRedirect('/')



def logoutFun(request):
    logout(request)
    return HttpResponseRedirect('/')