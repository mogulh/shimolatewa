from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"news/home.html")

def news(request):
    pass

def articles(request):
    pass

def gallery(request):
    pass

def news_detail(request, slug):
    pass

def article_detail(request, slug):
    pass

