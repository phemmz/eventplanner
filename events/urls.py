from django.conf.urls import include, url
from . import views

app_name = 'events'

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^event/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^contact/$', views.ContactView, name='contact'),
  url(r'^about/$', views.AboutView, name='about'),
]