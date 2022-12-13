from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

def user_authenticated(func):
    def wrap(request,*args,**kwargs):
        if 'token' not in request.session:
            if request.path == '/hong-bank/card-insert/':
                return func(request,*args,**kwargs)
            return redirect(reverse('account:InsertCard'))
        else:
            if request.path == '/hong-bank/card-insert/':
                return redirect('/hong-bank/')
            return func(request,*args,**kwargs)
    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap
            