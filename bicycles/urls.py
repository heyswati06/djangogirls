from django.conf.urls import url
from . import sale_views

urlpatterns = [
    url(r'^$', sale_views.salepost_list, name='salepost_list'),
    url(r'^post/(?P<pk>\d+)/$', sale_views.salepost_detail, name='salepost_detail'),
    url(r'^post/new/$', sale_views.salepost_new, name='salepost_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', sale_views.salepost_edit, name='salepost_edit'),
]