from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('type', 'price', 'status', 'issues')
        # fields = ('Date', 'Time', 'Submitted by', 'Shop', 'Maziwa Kubwa - 500ml', 'Premium Milk 500ml', 'Dairy Hope 200ml', 'Geocoords' )

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('type', 'price', 'status', 'issues')
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('type', 'price', 'status', 'issues')
        
# class MilkForm(forms.ModelForm):
#     class Meta:
#         model = Milk
#         fields = ('Date', 'Time', 'Submitted by', 'Shop', 'Maziwa Kubwa - 500ml', 'Premium Milk 500ml', 'Dairy Hope 200ml', 'Geocoords' )

