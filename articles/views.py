from django.shortcuts import render
from .models import Article

def article(request):
    return render(request,'articles/articles.html',{'art':Article.objects.all()})




# Create your views here.
