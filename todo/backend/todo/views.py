from django.db.models.query import QuerySet
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()    
    serializer_class = TodoSerializer