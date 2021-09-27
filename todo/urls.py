from django.urls import path
from todo.views import *

urlpatterns = [
    path('create',TodoCreateApiView.as_view(),name='create'),
    path('todo-list',TodoListApiView.as_view(),name='list'),
    path('<id>',TodoRetrieveUpdateDeleteApiView.as_view(),name='update-delete-retrieve')
]