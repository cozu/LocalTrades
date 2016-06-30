from django.conf.urls import url

from . import views

app_name = 'items'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    url('create', views.create, name='create'),
    url(r'^(?P<item_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<item_id>[0-9]+)/delete$', views.delete, name='delete')
]