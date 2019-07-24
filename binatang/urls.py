from django.urls import path
from . import views

urlpatterns = [
    path('',views.daftar_binatang, name='daftar_binatang'),
    path('twitter',views.twitter,name='twitter_amod'),
    path('input_hewan',views.input_hewan,name='input_hewan'),
]