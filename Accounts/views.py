from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from . import models as card_models
from . import forms as card_forms


def HomeView(request):
    return render(request,'home.html')

def InsertCardView(request):
    if request.method == 'POST': 
        form = card_forms.InsertCardForm(request.POST)
        if form.is_valid():
            try: 
                card = card_models.CardInfo.objects.get(card_number = form.cleaned_data['card_number'])
            except: 
                return render(request, 'insertcard.html', {'form': form, 'msg': 'Not a valid card number'})
            if card.pin != form.cleaned_data['pin']:
                form = card_forms.InsertCardForm()
                return render(request, 'insertcard.html', {'form': form, 'msg': 'Pin does not match'})
            else: 
                pk = card.pk
                return redirect(f"http://127.0.0.1:8000/bear-bank/{pk}/transaction/")
        else: 
            return render(request, 'insertcard.html', {'form': form, 'msg': 'Form not valid'})
    else:
        form = card_forms.InsertCardForm()
        return render(request, 'insertcard.html', {'form': form})

def RemoveCardView(request):
    return redirect('account:home')

def TransactionView(request,pk):
    form = card_forms.TransactionForm()
    card = card_models.CardInfo.objects.get(pk=pk)
    if request.GET:
        transaction = request.GET['category']
        if transaction == 'balance':
            return redirect(f"http://127.0.0.1:8000/bear-bank/{pk}/balance/")
        elif transaction == 'deposit':
            return redirect(f"http://127.0.0.1:8000/bear-bank/{pk}/deposit/")
        elif transaction == 'withdraw':
            return redirect(f"http://127.0.0.1:8000/bear-bank/{pk}/withdraw/")
    else:
        return render(request,'transaction.html',{'form':form})

def BalanceView(request,pk):
    card = card_models.CardInfo.objects.get(pk=pk)
    return render(request,"balance.html",{"card":card})

def DepositView(request,pk):
    if request.method == "POST":
        form = card_forms.DepositForm(request.POST)
        card = card_models.CardInfo.objects.get(pk=pk)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            card.account_number.balance += amount
            card.account_number.save()
            current_balance = card.account_number.balance
            return render(request,"deposit.html",{'balance':current_balance,'card':card})
        else:
            return render(request,'deposit.html',{'msg':"Not a valid amount"})
    else:
        form = card_forms.DepositForm()
        return render(request,'deposit.html',{'form':form})
        
            

def WithdrawView(request,pk):
    if request.method == "POST":
        form = card_forms.WithdrawForm(request.POST)
        card = card_models.CardInfo.objects.get(pk=pk)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount <= 0:
                form = card_forms.WithdrawForm()
                return render(request,"withdraw.html",{"form":form,'card':card,"msg":"Not a valid amount"})
            elif card.account_number.balance < amount:
                form = card_forms.WithdrawForm()
                return render(request,"withdraw.html",{'form':form,'card':card,'msg':"Insufficient Funds."})
            else:
                card.account_number.balance -=amount
                card.account_number.save()
                current_balance = card.account_number.balance 
                return render(request,'withdraw.html',{'form':form,'card':card,'balance':current_balance,"success_msg":"Funds Withdrawn Successfully"})
        else:
            form = card_forms.WithdrawForm()
            return render(request,"withdraw.html",{"form":form,'card':card,"msg":"Not a valid form"})
    else:
        form = card_forms.WithdrawForm()
        return render(request,"withdraw.html",{"form":form})
            
        