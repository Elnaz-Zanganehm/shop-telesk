from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from sabad.sabad import Sabad
from . import models
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from sabad.forms import SabadAddProductForm


def index(request):
    return render(request, 'index.html')


@login_required
def checkout(request):
    sabad = Sabad(request)
    if request.method == 'POST':
        order = models.Order.objects.create(customer=request.user)
        for item in sabad:
            models.OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            product_price=item['price'],
                                            product_count=item['product_count'],
                                            product_cost=Decimal(item['product_count']) * Decimal(item['price']))
        # order.customer = request.user
        # order.save()
        sabad.clear()
        return render(request, 'order_detail.html', {'order': order})

    return render(request,  'checkout.html', {'sabad': sabad})


def product(request, pk):
    product_detail = get_object_or_404(models.Product, id=pk)
    sabad_add_product_form = SabadAddProductForm()
    return render(request, 'product.html', {'product_detail': product_detail,
                                            'sabad_add_product_form': sabad_add_product_form})


def store(request):
    product_list = models.Product.objects.all()[:7]
    return render(request, 'store.html', {'product_list': product_list})


# LOGIN,LOGOUT,SIGNUP


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
    return render(request, 'login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect("shophummin:index")



