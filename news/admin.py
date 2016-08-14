#coding:utf-8
from django.contrib import admin
 
from .models import Column, Article,Users
 
 #栏目后台需要显示的字段
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro','nav_display','home_display')
 
 #文章后台需要显示的字段
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')

class UsersAdmin(admin.ModelAdmin):
 	list_display = ('username','password','headimg')
 
 #注册模型对象，这样就可以在后台直接显示这个对象，方便管理
admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Users,UsersAdmin)
