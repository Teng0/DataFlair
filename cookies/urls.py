from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
urlpatterns = [
    path('',views.index),
    path('setcookie', views.setcookie),
    path('getcookie', views.showcookie),
    path('deletecookie', views.delete_co),
    path('testcookie/', views.cookie_session),
    path('deletecookie2/', views.cookie_delete),
    path('create/',  views.create_session),
    path('access/',  views.access_session),
    path('delete/', views.delete_session)
]
