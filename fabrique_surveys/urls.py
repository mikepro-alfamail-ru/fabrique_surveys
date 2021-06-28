
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from surveys import views

router = routers.DefaultRouter()

router.register('surveys', views.SurveyViewSet)
router.register('questions', views.QuestionViewSet)
router.register('answervariants', views.AnswerVariantViewSet)
router.register('useranswers', views.UserAnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
