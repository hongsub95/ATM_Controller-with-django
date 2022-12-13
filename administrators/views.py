from django.shortcuts import render,redirect
from django.urls import reverse
from transactions import services
from .decorators import admin_authenticated
from . import forms as admin_form
from . import models as admin_models
from Accounts import models as account_models


def home(request):
    return render(request,"admin/Admin-home.html")


def AdminLogin(request):
    if request.method == "POST":
        form = admin_form.AdminLoginForm(request.POST)
        if form.is_valid():
            try:
                admin = admin_models.AdminUser.objects.get(username=form.cleaned_data['username'])
            except:
                form =admin_form.AdminLoginForm()
                return render(request,"admin/AdminLogin.html",{"form":form,"msg":"Incorrect Username"})
            if admin.password != form.cleaned_data['password']:
                form =admin_form.AdminLoginForm()
                return render(request,"admin/AdminLogin.html",{"form":form,"msg":"Incorrect Password"})
            request.session['admin_token'] = admin.username
            return redirect(reverse('administrator:admin-home'))
    else:
        form = admin_form.AdminLoginForm()
        return render(request,"admin/AdminLogin.html",{"form":form})

def AdminLogout(request):
    try:
        del request.session['admin_token']
        return redirect('/administrator/')
    except KeyError:
        pass      

@admin_authenticated
def CreateCardView(request):
    if request.method == "POST":
        form = admin_form.CreateCardForm(request.POST)
        if form.is_valid():
            is_AccNum = form.cleaned_data['is_AccNum']
            if is_AccNum == "0": #is_AccNum 초기값(initial)0으로 설정하여 계좌번호가 없으면 계좌번호 생성 함수 호출 
                try:
                    account = account_models.AccountInfo(account_number=services.CreateAccountNum(),balance=0)
                    account.save()
                except:
                    form = admin_form.CreateCardForm()
                    return render(request, 'admin/CreateCard.html', {'form': form, 'msg': 'Not a valid account number'})
            else: # 계좌번호가 있으면 0이 아닌 계좌번호를 입력
                account = account_models.AccountInfo.objects.get(account_number=int(is_AccNum))
            NewCardNum = services.CreateCardNum() # 카드번호 생성 함수 호출
            card = account_models.CardInfo(card_number=NewCardNum,pin=form.cleaned_data['pin'],name=form.cleaned_data['name'],phone_number=form.cleaned_data['phone_number'])
            card.account_number = account
            card.save()
            form = admin_form.CreateCardForm()
            return render(request, 'admin/CreateCard.html', {'form': form, 'msg': 'Card created succesfully!'})
        else: 
            return render(request, 'admin/CreateCard.html', {'form': form, 'msg': 'Form not valid'})
    else:
        form = admin_form.CreateCardForm()
        return render(request, 'admin/CreateCard.html', {'form': form})
            
            
            
            
