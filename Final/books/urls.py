from django.urls import path
from .views import TaskList,AddTask

urlpatterns = [
    path('', TaskList.as_view(), name= "home" ),
    path('task/', AddTask.as_view(), name='addtask'),

]


