from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def add_user(request):
    user = request.user
    if user is not None and user.is_authenticated and user.is_superuser:
        if request.method == 'POST':
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            if username and email and password and confirmpassword and first_name and last_name and password == confirmpassword:
                user, success = User.objects.get_or_create(username=username,
                                        first_name=first_name,
                                        last_name=last_name,             
                                        email=email,
                                        password=password,
                                        is_active=True,
                                        is_staff=True,
                                        is_superuser=False)
                if success:
                    user.set_password(password)
                    user.save()
                    # user successfully created
                    messages.success(request,"user successfully created")
                else:
                    # user already exists
                    messages.error(request,"user already exists")
            else:
                messages.error(request,"invalid input")
    else:
        messages.error(request,"You don't have permission to access user list")
    return render(request, 'add_user.html', {})

def list_users(request):
    userList = []
    user = request.user
    if user is not None and user.is_authenticated and user.is_superuser:
        users = User.objects.filter(is_staff=True,
                                is_superuser=False)
        for user in users.values():
            userList.append({"first_name": user["first_name"], "last_name": user["last_name"],
                "username": user["username"],  "email": user["email"],
                "is_active": user["is_active"]})
    else:
        messages.error(request,"You don't have permission to access user list")   
    return render(request, 'list_users.html', {"users": userList})