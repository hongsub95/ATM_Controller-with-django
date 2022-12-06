from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from . import models as card_models
from . import forms as card_forms
from .decorators import user_authenticated
from transactions import services

def HomeView(request):
    return render(request,'home.html')

@user_authenticated
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
                request.session['token'] = card.card_number
        else:
            return render(request, 'insertcard.html', {'form': form, 'msg': 'Form not valid'})
    else:
        form = card_forms.InsertCardForm()
        return render(request, 'insertcard.html', {'form': form})

def RemoveCardView(request):
    try:
        del request.session['token']
        return redirect('/hong-bank/')
    except KeyError:
        pass
    
@user_authenticated
def BalanceView(request,pk):
    try:
        card = card_models.CardInfo.objects.get(card_number=request.session['token'])
    except:
        return render(request,'deposit.html',{'msg':'User does not exist with that account number'})
    return render(request,"balance.html",{"card":card})

@user_authenticated
def DepositView(request):
    if request.method == "POST":
        form = card_forms.DepositForm(request.POST)
        if form.is_valid():
            try:
                card = card_models.CardInfo.objects.get(card_number=request.session['token'])
            except:
                return render(request,'deposit.html',{'msg':'User does not exist with that account number'})
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
        
@user_authenticated
def WithdrawView(request,pk):
    if request.method == "POST":
        form = card_forms.WithdrawForm(request.POST)
        if form.is_valid():
            try:
                card = card_models.CardInfo.objects.get(card_number=request.session['token'])
            except:
                return render(request,'deposit.html',{'msg':'User does not exist with that account number'})
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

@user_authenticated
def transaction_history(request):
    renderData = {
        'request':request,
        'path':'hong-bank/transaction-history/',
        'context':{
            'message':'',
            'history':[]
        }
    }
    card = services.getCardByNumber(request.session['token'])
    if not card:
        services.getMessageData(renderData['context'],'Issue getting CardNumber')
        return redirect(reverse('account:InsertCard'))
    transactions = services.getTransactionCard(card.card_number)
    if not transactions:
        services.getMessageData(renderData['context'],'You have no transactions')
        return services.renderpage(renderData)
    renderData['context']['history'] = transactions
    return services.renderpage(renderData)