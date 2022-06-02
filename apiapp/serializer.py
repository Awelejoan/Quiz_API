from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Option
        fields = ('question', 'a', 'b', 'c', 'd')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Answer
        fields = ('question', 'answer')
