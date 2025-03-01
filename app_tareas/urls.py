from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('', views.index, name='index'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/add_comment/', views.add_comment, name='add_comment'),
    path('task/<int:task_id>/edit/', views.edit_task, name='task_edit'),
    path('task/<int:task_id>/delete/', views.delete_task, name='task_delete'),
]