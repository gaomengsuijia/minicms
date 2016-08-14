# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse


#栏目模型对象 
@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    #控制是否导航显示
    nav_display = models.BooleanField('导航显示', default=False)

    #控制是否在首页显示
    home_display = models.BooleanField('首页显示',default=False)

    #得到网址
    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '栏目'     #显示模型在后台的名称
        verbose_name_plural = '栏目'    #如果模型是复数的显示名称，不指定的话，默认会加上s
        ordering = ['name']  # 按照哪个栏目排序
 
 #文章模型对象
@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')
 
    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)
 
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    #content = models.TextField('内容', default='', blank=True)
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
 
    published = models.BooleanField('正式发布', default=True)

    pub_date = models.DateTimeField('发表时间', auto_now=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)


     #得到网址
     
    def get_absolute_url(self):
        return reverse('article', args=(self.pk,self.slug,))
 
    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'


@python_2_unicode_compatible
    #用户表模型
class Users(models.Model):
    """用户表模型"""
    username = models.CharField('用户名',max_length=255)
    password = models.CharField('用户密码',max_length=255)
    headimg = models.FileField(upload_to='./upload')

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'
            