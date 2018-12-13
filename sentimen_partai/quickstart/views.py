from django.shortcuts import render
from django.contrib.auth.models import User, Group
import rest_framework
from rest_framework import viewsets, serializers
from sentimen_partai.quickstart.serializers import UserSerializer, GroupSerializer, SentimenPartaiSerializer
from . import sentimeter
from django.http import JsonResponse
from .forms import NameForm

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SentimenPartaiViewSet(viewsets.ModelViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = SentimenPartaiSerializer

    def list(self, request):
        if request.method == 'GET':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.GET)
            if form.is_valid():
                input = form.cleaned_data['q']
                data = sentimeter.primary(input)
                return JsonResponse(data)
