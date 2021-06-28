from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from rest_framework.serializers import ValidationError
from surveys.models import Survey, Question, QuestionTypes, AnswerVariant, UserAnswer
from surveys.serializers import SurveySerializer, QuestionSerializer, AnswerVariantSerializer, UserAnswerSerializer


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff


class AnswerVariantViewSet(ModelViewSet):
    queryset = AnswerVariant.objects.all()
    serializer_class = AnswerVariantSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "destroy", "update", "partial_update"]:
            permissions = [IsAdmin]
        else:
            permissions = []
        return [permission() for permission in permissions]


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "destroy", "update", "partial_update"]:
            permissions = [IsAdmin]
        else:
            permissions = []
        return [permission() for permission in permissions]


class SurveyViewSet(ModelViewSet):
    queryset = Survey.objects.select_related()
    serializer_class = SurveySerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "destroy", "update", "partial_update"]:
            permissions = [IsAdmin]
        else:
            permissions = []
        return [permission() for permission in permissions]

    def update(self, request, *args, **kwargs):
        # проверка на дату начала опроса, если указана, то запрещаем обновление
        if 'start_at' in request.data:
            raise ValidationError({
                'error': 'You must not change start_at field.',
            })

        return super().update(request, *args, **kwargs)


class UserAnswerViewSet(ModelViewSet):
    queryset = UserAnswer.objects.select_related()
    serializer_class = UserAnswerSerializer

    def create(self, request, *args, **kwargs):
        ...

    def update(self, request, *args, **kwargs):
        ...
