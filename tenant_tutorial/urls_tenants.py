from customers.views import TenantView
# from django.conf.urls import url
from django.urls import path

urlpatterns = [
    # url(r'^$', TenantView.as_view()),
    path('', TenantView.as_view()),
]