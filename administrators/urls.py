from django.urls import path
from . import views

app_name='administrator'

urlpatterns = [
    path('',views.home,name="admin-home"),
    path('login_admin/',views.AdminLogin,name="admin-login"),
    path('logout_admin/',views.AdminLogout,name="admin-logout"),
    path('create_card/',views.CreateCardView,name="create-card"),
    path('update_card/',views.UpdateCardView,name="update-card"),
    path('change_pin/',views.ResetPinView,name="change-pin"),
]
