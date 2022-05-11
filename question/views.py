from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import authentication_classes
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from .serializers import *
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from .models import Question, Answer, Result
from rest_framework.viewsets import ModelViewSet
from .permissions import *

User = get_user_model()


# Для Админимтраторов
class AdminUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = True
        serializer.save()


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrIsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminOrIsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


# Для пользователей

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.validated_data['is_staff'] = False
        serializer.save()


class ResultListCreateAPIView(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [BasicAuthentication, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class SomeListView(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = [BasicAuthentication, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
