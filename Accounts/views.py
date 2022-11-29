from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.generic import DetailView,FormView
from . import models as card_models
from . import forms as card_forms

def HomeView(request):
    return render(request,'home.html')

class InsertCardView(FormView):
    form_class = card_forms.InsertCardForm()
    template_name: str= ''
    def form_valid(self, form):
        card_number = form.cleaned_data['card_number']
        card = authenticate(self.request,card_number=card_number)