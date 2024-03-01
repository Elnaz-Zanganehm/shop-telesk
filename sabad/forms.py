from django import forms

PRODUCT_COUNT_CHOICES = [(i, str(i)) for i in range(1, 10)]


class SabadAddProductForm(forms.Form):
    product_count = forms.TypedChoiceField(choices=PRODUCT_COUNT_CHOICES,
                                           coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

# class OrdercompletionForm(forms.Form):
#     order_date = forms.DateTimeField(auto_now_add=True)
#     cpost = forms.CharField(max_length=10, blank=True)
#     address = forms.TextField(blank=True)
#     name = forms.TextField(blank=True)
#     family = forms.TextField(blank=True)
#     phon = forms.TextField(blank=True)




