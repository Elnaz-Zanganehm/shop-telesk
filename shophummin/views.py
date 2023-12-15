from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

def index(request):
    product_list = models.Product.objects.all()[:4]
    return render(request, 'index.html', {'product_list': product_list})

def checkout(request):
    return render(request, 'checkout.html')


def product(request):
    return render(request, 'product.html')





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shophummin:index')
                else:
                    return HttpResponse("اکانت شما غیرفعال است")
            else:
                return HttpResponse("اطلاعات شما نادرست است")
    else:
        form = LoginForm()
    return render(request, 'base.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect("shophummin:index")



