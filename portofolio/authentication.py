from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    template_name = "halaman/signin.html"
    pesan = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)    
            return redirect('/')
        else:
            pesan = "gagal login"
    context = {
        'pesan' : pesan
    }   

    return render(request, template_name, context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    template_name = "halaman/signup.html"
    pesan = ''
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name= request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        
        password = request.POST.get("password")
        retype_password = request.POST.get("retype_password")
        
        print(username, email, first_name, last_name, password, retype_password)
        
        if password == retype_password:
            check_user = User.objects.filter(username=username)
            if check_user.count() == 0:
                user_simpan = User.objects.create(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name,
                    is_active = True
                )
                user_simpan.set_password(password)
                user_simpan.save()
                
                return redirect('/')
                    
        
    context = {
        'pesan' : pesan
    }
    
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    return redirect("/")