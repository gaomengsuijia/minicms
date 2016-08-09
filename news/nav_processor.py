#coding:utf-8
from .models import Column
#从Column模型中过滤出所有显示在导航中的模型
nav_display_columns = Column.objects.filter(nav_display=True)
 
#上下文渲染器  可以将变量nav_display_columns在多个模板中使用 

def nav_column(request):
    return {'nav_display_columns': nav_display_columns}
