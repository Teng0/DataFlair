from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('other/', views.other, name = 'otherpage'),
    path('about/',views.about, name= 'about')
]
