from rest_framework import serializers
from .models import Survey, Question, AnswerVariant, UserAnswer


class AnswerVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = '__all__'


class AnswerVariantMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = ['title']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionMainSerializer(serializers.ModelSerializer):
    answervariant = AnswerVariantMainSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question', 'type', 'answervariant']

    def create(self, validated_data):
        answervariant_data = validated_data.pop('answervariant')
        question = Question.objects.create(**validated_data)
        for answervariant in answervariant_data:
            AnswerVariant.objects.create(quesion=question, **answervariant)
        return question


class SurveySerializer(serializers.ModelSerializer):
    question = QuestionMainSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', 'title', 'start_at', 'finish_at', 'description', 'question')

    def create(self, validated_data):
        question_data = validated_data.pop('question')
        survey = Survey.objects.create(**validated_data)
        for question in question_data:
            print(question)
            answervariant_data = question.pop('answervariant')
            question = Question.objects.create(survey=survey, **question)
            for answervariant in answervariant_data:
                AnswerVariant.objects.create(question=question, **answervariant)
        return survey


class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAnswer
        fields = '__all__'
