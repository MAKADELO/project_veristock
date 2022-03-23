from django import forms
from .models import Item, Product, Purchase
from .models import Product, Provider


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields =  '__all__'