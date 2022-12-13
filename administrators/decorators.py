from django.shortcuts import redirect
from django.urls import reverse

def admin_authenticated(function): 
    def wrap(request, *args, **kwargs): 
        if 'admin_token' not in request.session: 
            if request.path == 'administrator/login_admin/': 
                return function(request, *args, **kwargs)
            return redirect(reverse("administrator:admin-login"))
        else: 
            if request.path == '/administrator/login_admin/': 
                return redirect('/administrator/')
            return function(request,*args,**kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap