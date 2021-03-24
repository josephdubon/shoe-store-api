from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from nutshell_config.nutshell_app import serializers
from nutshell_config.nutshell_app import models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class NSManufacturerViewSet(viewsets.ModelViewSet):
    """
    API end point that allows Manufacturer to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = serializers.NSManufacturerSerializer


class NSShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API end point that allows Manufacturer to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = serializers.NSShoeTypeSerializer


class NSShoeColorViewSet(viewsets.ModelViewSet):
    """
    API end point that allows Manufacturer to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = serializers.NSShoeColorSerializer


class NSShoeViewSet(viewsets.ModelViewSet):
    """
    API end point that allows Manufacturer to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = serializers.NSShoeSerializer
