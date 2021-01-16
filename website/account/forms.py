from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class order_Form(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"



class customer_Form(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude= ['user']
class registerform(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
