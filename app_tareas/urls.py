from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('', views.index, name='index'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/', views.create_task, name='create_task'),
]