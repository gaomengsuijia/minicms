#coding:utf-8
from django.contrib import admin
 
from .models import Column, Article
 
 #栏目
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro','nav_display','home_display')
 
 #文章
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time')
 
 
admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)