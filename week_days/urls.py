from django.urls import path
from . import views

urlpatterns = [
    path('<int:todo_day>/', views.todo_day),
    path('<todo_name>/', views.todo_views_all),
]
