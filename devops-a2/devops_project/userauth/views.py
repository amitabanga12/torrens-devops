from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect(f"http://{request.get_host()}/") # Redirect to a success page.
            else:
                messages.error(request,"user is not active")
                return redirect(f"http://{request.get_host()}/userauth/login")
        else:
            messages.error(request,"Invalid username or password")
            return redirect(f"http://{request.get_host()}/userauth/login")
    else:
        # If method is GET, open Login View
        return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect(f"http://{request.get_host()}/")