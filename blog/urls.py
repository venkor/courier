from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
 	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
	url(r'^packages0/$', views.package_list_0, name='package_list_0'),
	url(r'^packages1/$', views.package_list_1, name='package_list_1'),
	url(r'^packages2/$', views.package_list_2, name='package_list_2'),
	url(r'^package/add/$', views.add_package, name='add_package'),
	url(r'^packages/(?P<pk>[0-9]+)/$', views.package_detail, name='package_detail'),
	#url(r'^package/new/$', views.package_new, name='package_new'),
	#url(r'^package/(?P<pk>[0-9]+)/edit/$', views.package_edit, name='package_edit'),
	#url(r'^package/(?P<pk>\d+)/remove/$', views.package_remove, name='package_remove'),
]
