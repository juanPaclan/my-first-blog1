from django.contrib.auth.models import User
from YOUR_APP.serializers import YOUR_MODEL_Serializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class PublicDataViewSet(viewsets.ModelViewSet):
    queryset = YOUR_MODEL.objects.all()
    serializer_class = YOUR_MODEL_Serializer

class ProtectedDataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = YOUR_MODEL.objects.all()
    serializer_class = YOUR_MODEL_Serializer
