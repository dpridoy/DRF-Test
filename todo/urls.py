from django.urls import path
from .views import TaskList, TaskDetails, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('task-list/', TaskList.as_view()),
    path('task-detail/<str:pk>', TaskDetails.as_view()),
    path('task-create/', TaskCreate.as_view()),
    path('task-update/<str:pk>', TaskUpdate.as_view()),
    path('task-delete/<str:pk>', TaskDelete.as_view()),
]