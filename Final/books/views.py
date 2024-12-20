from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Task

class TaskList(ListView):
    model = Task
    template_name = 'books/tasklist.html'

class AddTask(CreateView):
    model = Task
    template_name = 'books/addtask.html'
    fields = '__all__'

