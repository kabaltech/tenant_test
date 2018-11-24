# from django.conf.urls import url
from django.urls import path
from tenant_tutorial.views import HomeView


urlpatterns = [
    # url(r'^$', HomeView.as_view()),
    path('', HomeView.as_view()),
]
