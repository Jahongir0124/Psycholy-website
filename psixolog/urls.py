from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.register_view,name='register'),
    path('group/', views.group_view, name='group_view'),
    path('add_user/', views.add_user, name='add_user'),
    path('start_test/', views.start_test, name='start_test'),
    path('read/', views.read_article, name='read'),
]