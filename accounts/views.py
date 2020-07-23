from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .forms import User_register


def register(request):
    if request.method == 'POST':
        f = User_register(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,'Your Accouct is Created Successfully ')
            return redirect("accounts:login")
    else:
        f = User_register()
    return render(request, 'accounts/registration.html', {'form': f})

@login_required()
def delete_acc(request,username):
    request.user.delete()
    messages.warning(request,'Your Accouct has deleted')
    return redirect("/")


class User_Login(SuccessMessageMixin,LoginView):
    success_message="You have logged in Successfully"
