from django.urls import path
from .views import get_tasks, create_task
from . import views

urlpatterns = [
    path('tasks/', get_tasks, name="get_tasks"),
    path('tasks/create/', create_task, name="create_task"),
    path('', views.home, name='home'),
]