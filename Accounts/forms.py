from django import forms
from . import models

class InsertCardForm(forms.Form):
    card_number = forms.CharField(
        max_length = 16,
        label="Card Number"
    )
    pin = forms.CharField(
        max_length = 4,
        widget=forms.PasswordInput,
        label="PIN Number"
    )

class DepositForm(forms.Form):
    amount = forms.IntegerField(
        label = "Amount"
    )

class WithdrawForm(forms.Form):
    amount = forms.IntegerField(
        label = "Amount"
    )

class TransferForm(forms.Form):
    account_number = forms.IntegerField(
        label = "Account Number"
    )
    amount = forms.IntegerField(
        label = "Amount"
    )