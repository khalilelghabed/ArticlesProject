from django.urls import path
from .import views 
urlpatterns = [
    path('creercompte',views.account,name='acount'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout')
    
]
