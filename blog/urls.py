from django.conf.urls import url
from blog import views

urlpatterns = [
    
    url(r'^about/$', views.about , name='about'),
    url(r'^profile/$', views.profile , name='profile'),
    url(r'^login/$', views.login , name='login'),
    url(r'^profile_view/$', views.profile_view , name='profile_view'),
    url(r'^signup/$', views.signup , name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^post/list/$',views.post_list,name='post_list'), # to see all post
	url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='post_detail'), #to see a specific post
	url(r'^post/new/$',views.post_new,name='post_new'), # for creating new post
	url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='post_edit'),


]