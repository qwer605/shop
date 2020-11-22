from django.contrib import admin
from .models import *
from django.forms import ModelChoiceField, ModelForm


# Register your models here.


admin.site.register(Category)
admin.site.register(Notebook)
admin.site.register(Smartphone)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(CartProduct)