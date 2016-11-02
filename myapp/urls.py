from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.person_list, name='person_list'),
    #  url(r'^$', views.index, name='index'),
    url(r'^person/(?P<pk>\d+)/$', views.person_detail, name='person_detail'),
    url(r'^person/new/$', views.person_new, name='person_new'),
    url(r'^person/(?P<pk>\d+)/edit/$', views.person_edit, name='person_edit'),
]
