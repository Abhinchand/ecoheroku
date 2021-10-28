from .models import *
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','address','email','images','phone_number','pincode','district',)
        widgets = {

			}

class apiuserform(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2','address','phone_number']


class Form_product(forms.ModelForm):
    class Meta:
        model = product
        fields = [
        "product_name",
        "product_category",
        "price",
        "details",
        "images",

        ]
class Form_cart(forms.ModelForm):
    class Meta:
        model = cart
        fields = [
            "quantity",
        ]

class Form_address(forms.ModelForm):
    class Meta:
        model = delivery_address
        fields = [
            "d_name",
            "d_phone_number",
            "d_district",
            "d_pincode",
            "d_address",
            "d_pickup_time",
        ]

class Form_feedback(forms.ModelForm):
    class Meta:
        model = feedback
        fields = [
            'feedback_text'
        ]

