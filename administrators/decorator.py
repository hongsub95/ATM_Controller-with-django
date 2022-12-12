from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def admin_authenticated(function): 
    def wrap(request, *args, **kwargs): 
        if 'admin-token' not in request.session: 
            if request.path == '/administrator/admin_login': 
                return function(request, *args, **kwargs)
            return redirect('/administrator/admin-login')
        else: 
            if request.path == '/administrator/admin_login': 
                return redirect('/administrator/')
            return function(request,*args,**kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap