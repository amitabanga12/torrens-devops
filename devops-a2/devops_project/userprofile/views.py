from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def view_profile(request):
    user = request.user  
    return render(request, 'view_profile.html', {"user": user})