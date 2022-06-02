from django.shortcuts import render
from rest_framework. views import APIView
from rest_framework.response import Response
from .serializer import *

from .models import *

# Create your views here.
class Firstview(APIView):
    def get(self, request,*args, **kwargs):
        qs = Question.objects.all()
        serializer = QuestionSerializer(qs, many=True)
        return Response(serializer.data)

class Secondview(APIView):
    def get(self, request, *args, **kwargs):
        qs=Option.objects.all()
        serializer = OptionSerializer(qs, many=True)
        return Response(serializer.data)

class Thirdview(APIView):
    def get(self, request, *args, **kwargs):
        qs = Answer.objects.all()
        serializer = AnswerSerializer(qs, many=True)
        return Response(serializer.data)
    
