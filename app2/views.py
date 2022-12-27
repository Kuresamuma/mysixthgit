from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def uma(request):
    return HttpResponse("<h2> This is app2 uma view</h2>")
