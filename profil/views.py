from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from articles.models import Article 
@login_required
def afficher_profil(request):
    articles=Article.objects.filter(auteur=request.user)
    return render(request,'profil/profil.html',{'articles':articles})
# Create your views here.
