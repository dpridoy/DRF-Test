from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task


class TaskList(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetails(APIView):

    def get(self, request, pk):
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)


class TaskCreate(APIView):

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class TaskUpdate(APIView):

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class TaskDelete(APIView):

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response("Item deleted")
