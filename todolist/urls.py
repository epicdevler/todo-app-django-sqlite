
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='addTodo'),
    path('completed/<todo_id>', views.completedTodo, name='markCompleted'),
    path('cancel/<todo_id>', views.cancelTodo, name='markCancelled'),
    path('deletecompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deletecancelled', views.deleteCancelled, name='deleteCancelled'),
    path('deleteall', views.deleteAll, name='deleteAll'),
    path('clearStatus', views.clearStatus, name='clearStatus'),
]
