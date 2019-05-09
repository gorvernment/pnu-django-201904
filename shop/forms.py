from django import forms
from .models import Shop, Item


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        # widgets = {
        #     'address': ...,
        # }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
