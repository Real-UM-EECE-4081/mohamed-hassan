from django.contrib import admin
from ToDo_app.models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)