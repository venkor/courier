#from django.conf.urls import include, url, patterns
from django.conf.urls import url,include
from django.contrib.auth import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    #url(r'^blog/', include('blog.urls')),
]
