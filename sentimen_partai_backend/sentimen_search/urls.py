from django.conf.urls import url
from . import views

urlpatterns = [
    url('^/sentiment', views.index, name='sentimen_search'),
]
