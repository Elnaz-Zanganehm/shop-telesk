from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from . import forms
from .sabad import Sabad
from shophummin import models


@require_POST
def sabad_add(request, product_id):
    sabad =Sabad(request)
    product = get_object_or_404(models.Product, id=product_id)
    form = forms.SabadAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        sabad.add(product=product,
                  product_count=form_data['product_count'],
                  update_count=form_data['update'])
    return redirect(reverse('sabad:sabad_detail'))


def sabad_detail(request):
    sabad = Sabad(request)
    for item in sabad:
        item['update_product_count_form'] = forms.SabadAddProductForm(
            initial={'product_count': item['product_count'],
                     'update': True}
        )
    return render(request, 'sabad/detail.html', {'sabad': sabad})


def sabad_remove(request, product_id):
    sabad = Sabad(request)
    product = get_object_or_404(models.Product, pk=product_id)
    sabad.remove(product)
    return redirect(reverse('sabad:sabad_detail'))

