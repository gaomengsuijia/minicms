#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import Column,Article,Users
from .forms import Loginform,Zhuce
import json
# Create your views here.

#首页
def index(request):

    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    #获取登录cookie
    username = request.COOKIES.get('username','')
    
	
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        'username':username,
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
		pass
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
		pass
	return render(request,'news/register.html')

'''
#测试使用表单进行文件上传并保存到本地
def logintest(request):
	if request.method == 'POST':
		loginform = Loginform(request.POST,request.FILES)
		if loginform.is_valid():
			print loginform.cleaned_data['name']
			file_name = 'news/upload/' + loginform.cleaned_data['img_loader'].name
			with open(file_name,'wb') as f:
				s = loginform.cleaned_data['img_loader'].read()
				f.write(s)
			return HttpResponse('0k')

	else:
		loginform = Loginform()
	return render_to_response('news/test.html',{'loginform':loginform})
'''
#注册
def logintest(request):
	if request.method == 'POST':
		loginform = Loginform(request.POST,request.FILES)
		if loginform.is_valid():
			#print loginform.cleaned_data
			username = loginform.cleaned_data['username']
			password = loginform.cleaned_data['password']
			headimg  = loginform.cleaned_data['headimg']
			#实例化模型，保存数据
			#users = Users()
			'''
			第一种保存方法：
			users.username = username
			users.password = password
			users.headimg = headimg
			users.save()
			'''
			Users.objects.create(username=username,password=password,headimg=headimg)
			return HttpResponseRedirect('/zhuce')


	else:
		loginform = Loginform()
	return render_to_response('news/test.html',{'loginform':loginform})

#登录
def zhuce(request):
	if request.method == 'POST':
		zhuce = Zhuce(request.POST)
		if zhuce.is_valid():
			username = zhuce.cleaned_data['username']
			password = zhuce.cleaned_data['password']
			result = Users.objects.filter(username__exact=username,password__exact=password)
			if result:
				res = HttpResponseRedirect('/')
				#保存cookie到本地浏览器
				res.set_cookie('username',username,3600)
				return res
			else:
				return HttpResponseRedirect('/zhuce')

	else:
		zhuce = Zhuce()
	return render_to_response('news/zhuce.html',{'zhuce':zhuce})

	
#登出视图

def logout(request):
	res = HttpResponseRedirect('/')
	res.delete_cookie('username')
	return res


#测试向js中传递数据

def testjs(request):
	dict_js = {'name':'lily','age':50}
	return render_to_response('news/jstest.html',{'dict_js':json.dumps(dict_js)})



#小小的实例
# 注册  
# 改为ajax post   
def register(request):  
    if request.method == 'POST':  
         
        try:  
            reg_form = RegisterForm(request.POST)  
        except Exception as e:  
            print str(e)  
            # 登录失败 返回错误提示      
            err = "注册失败，请重试"  
            return result_response(request, err)   
  
        if reg_form.is_valid():  
            print "register success"  
            try:  
                username = reg_form.cleaned_data['username']  
                password = reg_form.cleaned_data['password']  
                user = UserProfile.objects.create(username = username, email = username,   
                password = make_password(password), is_active = True)  
                user.save()  
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式  
                # 验证成功登录  
                auth.login(request, user)  
                return result_response(request, "")  
            except Exception as e:  
                print str(e)  
                setFormTips(reg_form, "注册失败，请重试")  
        else:  
            print "register failed"  
  
            if request.POST.get('captcha_1') == "":  
                setFormTips(reg_form, "验证码不能为空")   
  
        # 登录失败 返回错误提示      
        err = getFormTips(reg_form)  
        return result_response(request, err)   