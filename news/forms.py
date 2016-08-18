#coding:utf-8
from django import forms

#登录test表单
class Loginform(forms.Form):
	username = forms.CharField(error_messages={"required": "用户名不能为空",})
	password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"请输入密码",}),error_messages={"required": "密码不能为空",})
	headimg = forms.FileField(error_messages={"required": "请选择需要上传的文件",}) 



#登录
class Zhuce(forms.Form):
	username = forms.CharField(error_messages={"required":"用户名不能为空"})
	password = forms.CharField(widget = forms.PasswordInput,error_messages={"required":"密码不能为空"})



#小小的实例 clean是在 is_valid()内部调用的，cleaned_data主要用来检查字段是否符合定义的格式，如果是则返回其值，下面举个简单的例子来感受下。
class RegisterForm(forms.Form):  
    ''''' 
    注册 
    '''  
    username = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入邮箱账号", "value": "", "required": "required",}),  
                              max_length=50,error_messages={"required": "用户名不能为空",})  
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码", "value": "", "required": "required",}),  
                              min_length=8, max_length=50,error_messages={"required": "密码不能为空",})  
   
    def clean(self):  
          
         # 用户名  
        try:            
            username=self.cleaned_data['username']  
        except Exception as e:  
            print 'except: '+ str(e)  
            raise forms.ValidationError(u"注册账号需为邮箱格式")      
  
  
        # 登录验证          
        is_email_exist = UserProfile.objects.filter(email=username).exists()   
        is_username_exist = UserProfile.objects.filter(username=username).exists()   
        if is_username_exist or is_email_exist:  
            raise forms.ValidationError(u"该账号已被注册")  
  
  
        # 密码  
        try:  
            password=self.cleaned_data['password']  
        except Exception as e:  
            print 'except: '+ str(e)  
            raise forms.ValidationError(u"请输入至少8位密码");  
  
  
        return self.cleaned_data    
