from django.urls import path
from . import views


urlpatterns = [
    path('',views.check_user,name='check_user'),
    path('',views.logout_view,name='logout_view')
]