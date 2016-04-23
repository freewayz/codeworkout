from django.forms.forms import Form
from django import  forms

__author__ = 'peter'





class PayPalCheckoutForm(Form):
    first_name = forms.CharField(label="Firstname")
    last_name = forms.CharField(label="Lastname")
    amount  = forms.CharField(label="Payment Amount")
