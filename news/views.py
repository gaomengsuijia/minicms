#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Column,Article
# Create your views here.

def index(request):

    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
 
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        })


def column_detail(request,column_slug):
	column = Column.objects.get(slug=column_slug)
	return render(request, 'news/column.html', {'column': column})



def article_detail(request,pk,article_slug):
	article = Article.objects.get(pk=pk)

	#判断当网址改变的时候进行重定向到新的网址
	if article.slug != article_slug:
		return redirect(article, permanent=True)

	return render(request, 'news/article.html', {'article': article})



def login(request):
	return render(request,'news/login.html')