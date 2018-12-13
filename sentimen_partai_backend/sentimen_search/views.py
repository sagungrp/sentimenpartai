from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from . import sentimeter

def sentiment(self, request):
    if request.GET.get == 'GET':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.GET)
        if form.is_valid():
            input = form.cleaned_data['q']
            data = sentimeter.primary(input)
            return JsonResponse(data)