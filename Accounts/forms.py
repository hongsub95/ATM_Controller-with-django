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


class TransactionForm(forms.Form):
    CATEGORY_CHOICE= (("balance","balance"),("deposit","deposit"),("withdraw","withdraw"))
    category =forms.ChoiceField(choices = CATEGORY_CHOICE,required=True)

class DepositForm(forms.Form):
    amount = forms.IntegerField(
        label = "Amount"
    )

class WithdrawForm(forms.Form):
    amount = forms.IntegerField(
        label = "Amount"
    )