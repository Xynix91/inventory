from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/list/', views.list, name='list'),
    path('<int:user_id>/details/<int:film_id>/', views.details, name='details')
]
