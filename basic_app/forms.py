from django import forms
from django.contrib.auth.models import User
from .models import PCategory, Products, UserProfileInfo


class UserForm(forms.ModelForm):  
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "password", "email")

class UserProfileInfoForm(forms.ModelForm):
    
    class Meta:
        model = UserProfileInfo
        fields = ("user_job", "national_id")

class ProductForm(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset= PCategory.order_by('cat_name'))
    category = forms.ModelChoiceField(queryset= PCategory.objects.all())
    product_image = forms.ImageField()
    class Meta:
        model = Products
        fields = ("category", "product_name", "product_image")
