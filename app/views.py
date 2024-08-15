from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def starbucks(request):
    return HttpResponse('worst chai is available in starbucks')