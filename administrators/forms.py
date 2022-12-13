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
    # 계좌번호가 존재하면 계좌번호 입력, 없으면 초기값 0으로 제출
    is_AccNum = forms.CharField(
        label="Account Number",
        initial="0"
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