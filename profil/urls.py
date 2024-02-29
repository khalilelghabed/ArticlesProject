from django.urls import path
from . views import afficher_profil

urlpatterns = [
   path('',afficher_profil,name='profil')
]
