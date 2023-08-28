from django.shortcuts import render
import json
# Create your views here.

from django.contrib.auth.models import User, Group, Permission, PermissionsMixin
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from users.serializers import UserSerializer, GroupSerializer, PermissionSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.forms.models import model_to_dict

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

class CheckPermissionViewSet(views.APIView):
    
    def get(self, request):

        object = request.GET.get('object', '')
        user = request.GET.get('user', '')
        action = request.GET.get('action', '')
        user = User.objects.get(pk=int(user))
        user_permissions = PermissionsMixin.get_user_permissions(user)
        permission_code = f"users.{action}_{object}"
        
        return Response({"granted": permission_code in user_permissions})
