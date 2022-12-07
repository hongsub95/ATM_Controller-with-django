from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from . import models as card_models
from . import forms as card_forms
from .decorators import user_authenticated
from transactions import services
from transactions import models as transaction_models

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
                return render(request, 'account/insertcard.html', {'form': form, 'msg': 'Not a valid card number'})
            if card.pin != form.cleaned_data['pin']:
                form = card_forms.InsertCardForm()
                return render(request, 'account/insertcard.html', {'form': form, 'msg': 'Pin does not match'})
            else: 
                request.session['token'] = card.card_number
                return redirect('/hong-bank/')
        else:
            return render(request, 'account/insertcard.html', {'form': form, 'msg': 'Form not valid'})
    else:
        form = card_forms.InsertCardForm()
        return render(request, 'account/insertcard.html', {'form': form})

def RemoveCardView(request):
    try:
        del request.session['token']
        return redirect('/hong-bank/')
    except KeyError:
        pass
    
@user_authenticated
def BalanceView(request):
    try:
        card = card_models.CardInfo.objects.get(card_number=request.session['token'])
    except:
        return render(request,'account/deposit.html',{'msg':'User does not exist with that account number'})
    return render(request,"account/balance.html",{"card":card})

@user_authenticated
def DepositView(request):
    if request.method == "POST":
        form = card_forms.DepositForm(request.POST)
        if form.is_valid():
            try:
                card = card_models.CardInfo.objects.get(card_number=request.session['token'])
            except:
                return render(request,'account/deposit.html',{'msg':'User does not exist with that account number'})
            amount = form.cleaned_data['amount']
            card.account_number.balance += amount
            card.account_number.save()
            current_balance = card.account_number.balance
            transaction = transaction_models.transaction(status ='complete',response_code='200',transaction_type='deposit')
            transaction.card_number = card
            transaction.save()
            return render(request,"account/deposit.html",{'balance':current_balance,'card':card})
        else:
            return render(request,'account/deposit.html',{'msg':"Not a valid amount"})
    else:
        form = card_forms.DepositForm()
        return render(request,'account/deposit.html',{'form':form})
        
@user_authenticated
def WithdrawView(request):
    if request.method == "POST":
        form = card_forms.WithdrawForm(request.POST)
        if form.is_valid():
            try:
                card = card_models.CardInfo.objects.get(card_number=request.session['token'])
            except:
                return render(request,'account/deposit.html',{'msg':'User does not exist with that account number'})
            amount = form.cleaned_data['amount']
            if amount <= 0:
                form = card_forms.WithdrawForm()
                return render(request,"account/withdraw.html",{"form":form,'card':card,"msg":"Not a valid amount"})
            elif card.account_number.balance < amount:
                form = card_forms.WithdrawForm()
                return render(request,"account/withdraw.html",{'form':form,'card':card,'msg':"Insufficient Funds."})
            else:
                card.account_number.balance -=amount
                card.account_number.save()
                current_balance = card.account_number.balance 
                transaction = transaction_models.transaction(status ='complete',response_code='200',transaction_type='withdraw')
                transaction.card_number = card
                transaction.save()
                return render(request,'account/withdraw.html',{'form':form,'card':card,'balance':current_balance,"success_msg":"Funds Withdrawn Successfully"})
        else:
            form = card_forms.WithdrawForm()
            return render(request,"account/withdraw.html",{"form":form,'card':card,"msg":"Not a valid form"})
    else:
        form = card_forms.WithdrawForm()
        return render(request,"account/withdraw.html",{"form":form})

@user_authenticated
def TransferView(request):
    if request.method == "POST":
        form = card_forms.TransferForm(request.POST)
        if form.is_valid():
            accNum = form.cleaned_data['account_number']
            amount = form.cleaned_data['amount']

            if amount < 0:
                form = card_forms.TransferForm()
                return render(request,'account/transfer.html',{'form':form,'msg': 'Not a valid transfer amount'})
            try:
                rec_accNum = card_models.AccountInfo.objects.get(account_number=accNum)
            except:
                form = card_forms.TransferForm()
                return render(request,'account/transfer.html',{'form':form,'msg':'User does not exist with that account number.'})
            card = card_models.CardInfo.objects.get(card_number=request.session['token'])
            if card.account_number.balance < amount:
                form = card_forms.TransferForm()
                return render(request, 'user/cash-transfer.html', {
                    'form': form,
                    'msg': 'Insufficient Funds.'
                })
            else:
                card.account_number.balance -= amount
                rec_accNum.balance +=amount
                card.save()
                rec_accNum.save()
                transaction = transaction_models.transaction(status='complete',response_code='200',transaction_type='transfer')
                transaction.card_number=card
                transaction.save()
                return render(request, 'account/transfer.html', {
                    'msg': 'Funds Transfered Successful',
                    'form': form
                })
        else: 
            form = card_forms.TransferForm()
            return render(request, 'account/transfer.html', {
            'form': form,
            'msg': 'Form is not valid.'
        })
    else:
        form = card_forms.TransferForm()
        return render(request, 'account/transfer.html', {
            'form': form
        })
            
@user_authenticated
def transaction_history(request):
    renderData = {
        'request':request,
        'path':'transaction/transaction-history.html',
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