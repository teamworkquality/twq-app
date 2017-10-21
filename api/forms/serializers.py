from rest_framework import serializers
from .models import Form, Question

class FormSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ('name', 'created_at', 'has_time_limit', 'time_limit', 'questions')



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "_all_"