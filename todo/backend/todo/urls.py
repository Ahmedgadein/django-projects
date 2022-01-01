from django.urls import path
from .views import DetailTodo, ListTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view())
]
