from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.http import HttpResponse


@api_view(['GET'])
def home(request):
    question_obj = Question.objects.all()
    serializer = QuizSerializer(question_obj, many=True)
    return Response({'status': 200, "message": 'hello', 'payload': serializer.data})
