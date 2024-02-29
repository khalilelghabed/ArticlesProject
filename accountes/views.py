from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
def account(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password1")
        confirmer=request.POST.get("password2")
        if password==confirmer:
            utilisateur=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            utilisateur.save()
            messages.success(request,"compte a été crée avec succes")
            return redirect('acount')

        else:
            messages.error(request,'les deux messages sont differents')
            return redirect('acount')
    return render(request,'login/ceation_compte.html')
def login_user(request):
 if request.method=='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    utilisateur=authenticate(request,username=username,password=password)
    if utilisateur is not None:
        login(request,utilisateur)
        return redirect('homme')
    else:
        return render(request, 'login/connextion.html', {'error_message': 'Invalid credentials'})
 return render(request,'login/connextion.html')

def logout_user(request):
    logout(request)
    return redirect('homme')


    


    