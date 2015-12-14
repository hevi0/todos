from rest_framework import status, permissions, mixins, generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from models import Todos, TodoItem
from serializers import TodosSerializer, TodoItemSerializer
from permissions import IsOwner, IsOwnerOfTodoItem

class TodosView(
                mixins.ListModelMixin,
                mixins.DestroyModelMixin,
                mixins.RetrieveModelMixin,
                generics.GenericAPIView
                ):
    def get(self, request, todos_id=None, format=None, *args, **kwargs):
        if todos_id is None:
            return self.list(request, format, *args, **kwargs)
        else:
            return self.retrieve(request, todos_id, format, *args, **kwargs)

    def post(self, request, format=None):
        serializer = TodosSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, todos_id, format=None):
        todos = Todos.objects.get(pk=todos_id)
        serializer = TodosSerializer(todos, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    serializer_class = TodosSerializer
    lookup_url_kwarg = 'todos_id'

class TodoItemView(
                mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.DestroyModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                generics.GenericAPIView
                ):
    permission_classes = (IsAuthenticated, IsOwnerOfTodoItem)
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    serializer_class = TodoItemSerializer
    lookup_url_kwarg = 'todoitem_id'

    def get_queryset(self):
        return TodoItem.objects.filter(todos_id=self.kwargs['todos_id'])

    def get(self, request, todoitem_id=None, *args, **kwargs):
        if todoitem_id is None:
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(self, todoitem_id, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = TodoItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(todos_id=kwargs['todos_id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, todoitem_id, *args, **kwargs):
        todoitem = TodoItem.objects.get(pk=todoitem_id)
        serializer = TodoItemSerializer(todoitem, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
