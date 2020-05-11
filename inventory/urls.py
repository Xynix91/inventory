from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login-failed/', views.login_failed, name='login-failed'),
    path('verify/', views.verify, name='verify'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('create-action/', views.create_action, name='create-action'),
    path('details/<int:film_id>/', views.details, name='details'),
    path('edit/<int:film_id>/', views.edit, name='edit'),
    path('delete/<int:film_id>/', views.delete, name='delete'),
]
