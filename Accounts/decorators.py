from django.shortcuts import redirect,reverse
from django.http import HttpResponseRedirect

def user_authenticated(func):
    def wrap(request,*args,**kwargs):
        if 'token' not in request.session:
            if request.path == '/hong-bank/card-insert/':
                return func(request,*args,**kwargs)
            return redirect(reverse('account:InsertCard'))
        else:
            if request.path == '/hong-bank/InsertCard':
                return redirect('/hong-bank/')
            return func(request,*args,**kwargs)
    return wrap
            