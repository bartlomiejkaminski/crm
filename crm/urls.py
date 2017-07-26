from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('my_crm.urls')),
]