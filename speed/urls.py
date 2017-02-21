from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.speed_list, name='speed_list'),
    url(r'^speed/new/$', views.speed_new, name='speed_new'),  
    url(r'^speed/(?P<pk>\d+)/$', views.speed_detail, name='speed_detail'),
]