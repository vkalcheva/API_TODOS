from rest_framework import generics as rest_generic_views, permissions

from todo_app.api_todos.models import Todo, Category
from todo_app.api_todos.serializers import TodoForCreateSerializer, TodoForListSerializer, CategorySerializer


class ListCreateTodoApiView(rest_generic_views.ListCreateAPIView):
    queryset = Todo.objects.all()

    create_serializer_class = TodoForCreateSerializer
    list_serializer_class = TodoForListSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset



class ListCategoriesApiView(rest_generic_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )





