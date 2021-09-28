from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TodoCreateApiView(generics.CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class TodoListApiView(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['id','title']
    search_fields = ['id','title']
    ordering_fields = ['id','title']

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)

class TodoRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)