from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student,Homework
from .serializers import StudentSerializer,HomeworkSerializer


def index(request):
    return HttpResponse('index')

class Students(APIView):
    def get(self, request):
        students = Student.objects.all()
        return Response({'students':StudentSerializer(students,many=True).data})

    def post(self, request):

        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'students':serializer.data})

    def put(self, request ,*args, **kwargs):
        pk = kwargs['pk']
        if not pk:
            return Response({'error':'pk required'})
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error':'No this user'})
        serializer = StudentSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'students':serializer.data})


class Homeworks(APIView):
    def get(self,request):
        homework = Homework.objects.all()
        return Response({'homeworks':HomeworkSerializer(homework,many=True).data})

    def put(self,request,*args,**kwargs):
        pk = kwargs['pk']
        if not pk:
            return Response({'error':'pk is needed'})
        try:
            instance = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({'error':'no any homeworks. feel free today bro'})
        serializer = HomeworkSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'homeworks': serializer.data})

    def delete(self,request,*args,**kwargs):
        pk = kwargs['pk']
        all = Homework.objects.all()
        try:
            hw = Homework.objects.get(pk=pk)
            hw.delete()
            return Response({'homeworks':all.values()})
        except Homework.DoesNotExist:
            return Response({'msg':'Hehe not here'})