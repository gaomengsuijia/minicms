from django.conf.urls import patterns, include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minicms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/',include(DjangoUeditor_urls)),

    url(r'^$', 'news.views.index', name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', 'news.views.column_detail', name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', 'news.views.article_detail', name='article'),
    url(r'^login/$', 'news.views.login', name='login'),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)