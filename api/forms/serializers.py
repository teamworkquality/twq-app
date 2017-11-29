from rest_framework import serializers
from .models import Form, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text', 'reversed')


class FormSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    time_limit = serializers.DateTimeField(required=False)

    class Meta:
        model = Form
        fields = ('name', 'has_time_limit', 'time_limit', 'questions', 'min', 'max')

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        form = Form.objects.create(**validated_data)
        for question_data in questions_data:
            Question.objects.create(form=form, **question_data)
        return form


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"
