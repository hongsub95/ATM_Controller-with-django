from django import forms

class AdminLoginForm(forms.Form): 
    username = forms.CharField(
        label = 'username', 
        max_length = 20
    )
    password = forms.CharField(
        label = 'Password', 
        max_length = 20, 
        widget = forms.PasswordInput()
    )
class CreateCardForm(forms.Form):
    is_AccNum = forms.BooleanField(
        label="If you have Account Number,ignore",
        default=False
    )
    name = forms.CharField(
        label="name",
        max_length=20
    ) 
    pin = forms.CharField(
        label = 'pin', 
        max_length = 20, 
        widget = forms.PasswordInput()
    )
    phone_number = forms.CharField(
        max_length=12,
        label = "phone_number"
    )