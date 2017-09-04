from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.index),
   url(r'^pesantour/', views.destinasi),
   url(r'^pesantour/(?P<id>\d+)$', views.pilih_reservasi)
]