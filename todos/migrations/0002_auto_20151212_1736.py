# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='todoList',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todo_list',
            field=models.ForeignKey(related_name='todo_items', default=None, to='todos.TodoList'),
            preserve_default=False,
        ),
    ]
