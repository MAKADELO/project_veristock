from django import forms
from .models import Item, Product, Purchase, Sale, Provider, Devolution


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cost_sale', 'brand', 'reference', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ingrese el nombre del producto',
        })

        self.fields['cost_sale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ingrese el precio del producto',
        })
        
        self.fields['brand'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la marca del producto',
        })

        self.fields['reference'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la referencia del producto',
        })

        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la cantidad',
        })


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['warranty_start', 'warranty_end', 'remarks', 'serial', 'state', 'product', 'purchase', 'cost_sale']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['warranty_start'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el inicio de la garantia',
        })

        self.fields['warranty_end'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el final de la garantia',
        })

        self.fields['remarks'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Observaciones',
        })

        self.fields['serial'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Serial',
        })

        self.fields['state'].widget.attrs.update({
            'class': 'form-select',
            'default': 'Seleccione una opción',
        })

        self.fields['product'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Producto',
        })

        self.fields['purchase'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Compra',
        })

        self.fields['cost_sale'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Costo venta',
        })
        
class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['NIT', 'name', 'phone', 'address', 'email_address']

        self.fields['NIT'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el NIT del proveedor',
        })

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'nombre del proveedor',
        })

        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Telefono del proveedor',
        })

        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Direccion del proveedor',
        })

        self.fields['email_address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Correo electronico del proveedor',
        })

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields =  ['date', 'quantity', 'purchase_cost', 'provider', 'invoice_number']

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese fecha de la compra',
        })

        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la cantidad',
        })

        self.fields['purchase_cost'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el costo de la compra',
        })

        self.fields['provider'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Ingrese el proveedor',
        })
        
        self.fields['invoice_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Numero de factura',
        })

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields =  ['invoice', 'date', 'quantity', 'total', 'customer', 'user', 'item']

        self.fields['invoice'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Numero de factura',
        })

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese fecha de venta',
        })

        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'cantidad',
        })

        self.fields['total'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'total',
        })

        self.fields['customer'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Ingrese el cliente',
        })

        self.fields['user'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Ingrese el usuario',
        })

        self.fields['item'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Item',
        })
        
class DevolutionForm(forms.ModelForm):

    class Meta:
        model = Devolution
        fields =  ['date', 'reason', 'remarks', 'item']

        self.fields['date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la fecha de la devolucion',
        })

        self.fields['reason'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Motivo de la devolucion',
        })

        self.fields['remarks'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Observaciones',
        })

        self.fields['item'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Item',
        })