
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='addTodo'),
    path('completed/<todo_id>', views.completedTodo, name='markCompleted'),
    path('deletecompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteall', views.deleteAll, name='deleteAll'),
]
