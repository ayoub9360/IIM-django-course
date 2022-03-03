from django.forms import ModelForm
from .models import Product


class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('stock',)

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'imageUrl', 'price', 'stock',)