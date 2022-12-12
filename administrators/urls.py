from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="admin-home"),
    path('add_card/',views.CreateCardView,name="admin-add-card")
]
