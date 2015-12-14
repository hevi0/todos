# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0002_auto_20151212_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='todo_list',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todos',
            field=models.ForeignKey(related_name='todo_items', default=None, to='todos.Todos'),
            preserve_default=False,
        ),
    ]
