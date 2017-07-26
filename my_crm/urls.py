from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^companies/$', views.companies_list),
    url(r'^companies/create$', views.companies_create),
    url(r'^users/$', views.users_list),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
]