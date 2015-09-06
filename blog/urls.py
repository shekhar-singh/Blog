from django.conf.urls import url
from blog import views

urlpatterns = [
    
    url(r'^about/$', views.about , name='about'),
    url(r'^profile/$', views.profile , name='profile'),
    url(r'^login/$', views.login , name='login'),
    url(r'^profile_view/$', views.profile_view , name='profile_view'),



]