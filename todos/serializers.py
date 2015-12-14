from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Todos, TodoItem

# Serializers define the API representation.

class ItemHyperlink(serializers.HyperlinkedRelatedField):
    # We define these as class attributes, so we don't need to pass them as arguments.
    view_name = 'item-detail'
    #queryset = TodoItem.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'todos_id': obj.todos.id,
            'todoitem_id': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    #def get_object(self, view_name, view_args, view_kwargs):
    #    lookup_kwargs = {
    #       'list_id': view_kwargs['list_id'],
    #       'pk': view_kwargs['pk']
    #    }
    #    return self.get_queryset().get(**lookup_kwargs)

class TodosSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    #user = serializers.HyperlinkedRelatedField(many=False, read_only=True)
    title = serializers.CharField()
    todo_items = ItemHyperlink(many=True, read_only=True )

    class Meta:
        model = Todos
        fields = ('id', 'title', 'todo_items' )

class TodoItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    todos = serializers.HyperlinkedRelatedField(view_name='todos-detail', many=False, read_only=True, lookup_url_kwarg='todos_id')
    title = serializers.CharField()
    completed = serializers.BooleanField()
    description = serializers.CharField()

    class Meta:
        model = TodoItem
        fields = ('id', 'todos', 'title', 'description', 'completed', )
