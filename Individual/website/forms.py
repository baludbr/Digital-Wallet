from django import forms
from .models import Register_Login,Transaction_History,Query
class Register_Details(forms.ModelForm):
    class Meta:
        model=Register_Login
        fields=['id','name','email','password','age','balance']
class Transaction_History_Details(forms.ModelForm):
    class Meta:
        model=Transaction_History
        fields=['id1','category','type_amount','amount','balance']
class Query_submit(forms.ModelForm):
    class Meta:
        model=Query
        fields=['query','problem']