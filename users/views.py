from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        print("Invalid username or password")
    return render(request, "users/login.html")
def user_logout(request):
    logout(request)
    return render(request, 'users/user_logout.html')