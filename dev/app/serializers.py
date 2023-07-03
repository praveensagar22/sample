from rest_framework import serializers
from .models import Question


class QuizSerializer(serializers.ModelSerializer):
    options = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'options', 'answer']
