from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from user.admin import UserCreationForm 

def user_login(request):
    "User login page"

    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
        template_name = "login.html"
        return render(request, template_name)
    
def register(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            print(request.POST)
            if form.is_valid():
                user_inst = form.save()
                user = form.cleaned_data.get('username')

                # Custom.objects.create(user=user_inst)
                return redirect('login')
        context = {'form': form}
        template_name = "register.html"
        return render(request, template_name, context)
    
def user_logout(request):
    "User logout"
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/')
    
