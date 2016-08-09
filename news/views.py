#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Column,Article,Users
# Create your views here.

#首页
def index(request):

    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
 
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        })

#栏目详情
def column_detail(request,column_slug):
	column = Column.objects.get(slug=column_slug)
	return render(request, 'news/column.html', {'column': column})

#文章详情

def article_detail(request,pk,article_slug):
	article = Article.objects.get(pk=pk)

	#判断当网址改变的时候进行重定向到新的网址
	if article.slug != article_slug:
		return redirect(article, permanent=True)

	return render(request, 'news/article.html', {'article': article})


#登录视图
def login(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username','username')
		password = request.REQUEST.get('password','password')
		result = Users.objects.get(username=username)
		if result.password == password:
			return render(request,'index.html')
		else:
			return render(request,'news/login.html')
	else:
		return render(request,'news/login.html')




#注册视图
def register(request):
	if request.method == 'POST':
		username = request.REQUEST.get('username','username')
		password = request.REQUEST.get('password','password')
		confirm_password = request.REQUEST.get('confirm_password','confirm_password')
		if password !=confirm_password:
			pass
		elif username == '' or password == '':
			pass
		else:
			result = Users.objects.get_or_create(username=username,password=password)
			if result[1]:
				return HttpResponse('<h1>注册成功</h1>')
			else:
				return HttpResponse('<h1>该用户已经注册</h1>')
	else:
		return render(request,'news/register.html')