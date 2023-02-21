from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Create your views here.
class SingleMenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})
