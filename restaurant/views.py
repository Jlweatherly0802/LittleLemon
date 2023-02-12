from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'index2.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryser = Menu.objects.all()
    serializer_class = MenuSerializer 
