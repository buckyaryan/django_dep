from django.urls import path
from start_app import views

app_name = 'start_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('relative/',views.relative, name='relative'),
    path('other/',views.other, name='other'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login, name='user_login'),
]