from django.shortcuts import render  # noqa: F401
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import UserModel
from .serializer import UserSerialzer
# Create your views here.


# Use generics to add GET endpoint in the shorter form.
class ListAPIUserModel(ListAPIView):
    queryset = UserModel.objects.order_by("date").all()
    serializer_class = UserSerialzer


# Use generics to add POST endpoint in the shorter form.
class CreateAPIUserModel(CreateAPIView):
    queryset = UserModel.objects.order_by("date").all()
    serializer_class = UserSerialzer
