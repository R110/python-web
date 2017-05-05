from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entry_url>\w+)/$', views.entry, name='entry'),
]
