from django.shortcuts import render
from transactions import services
from .decorator import admin_authenticated
from . import forms as admin_form
from Accounts import models as account_models

@admin_authenticated
def home(request):
    return render(request,"admin/Admin-home.html")

@admin_authenticated
def AdminLogin(request):
    pass

@admin_authenticated
def CreateCardView(request):
    if request.method == "POST":
        form = admin_form.CreateCardForm(request.POST)
        if form.is_valid():
            is_AccNum = form.cleaned_data['is_AccNum']
            if is_AccNum:
                try:
                    account = account_models.AccountInfo.objects.get(account_number=is_AccNum)
                except:
                    form = admin_form.CreateCardForm()
                    return render(request, 'administrator/CreateCard.html', {'form': form, 'msg': 'Not a valid account number'})
            else:
                account = account_models.AccountInfo(account_number=services.CreateAccountNum(),balance=0)
            NewCardNum = services.CreateCardNum
            card = account_models.CardInfo(card_number=NewCardNum,pin=form.cleaned_data['pin'],name=form.cleaned_data['name'],phone_number=form.cleaned_data['phone_number'])
            card.account_number = account
            card.save()
            form = admin_form.CreateCardForm()
            return render(request, 'administrator/CreateCard.html', {'form': form, 'msg': 'Card created succesfully!'})
        else: 
            return render(request, 'administrator/CreateCard.html', {'form': form, 'msg': 'Form not valid'})
    else:
        form = admin_form.CreateCardForm()
        return render(request, 'administrator/CreateCard.html', {'form': form})
            
            
            
            
