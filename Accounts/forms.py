from django import forms

class InsertCardForm(forms.Form):
    card_number = forms.CharField(
        max_length = 16,
        label="카드번호"
    )
