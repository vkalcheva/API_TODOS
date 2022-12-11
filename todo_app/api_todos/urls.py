from django.urls import path

from todo_app.api_todos.views import ListCreateTodoApiView, ListCategoriesApiView

urlpatterns = (
    path('', ListCreateTodoApiView.as_view(), name='api list todos'),
    path('categories/', ListCategoriesApiView.as_view(), name='api list categories'),
)