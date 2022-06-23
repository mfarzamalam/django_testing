from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request):
    return HttpResponse("OK")


def author_detail(request, pk):
    return HttpResponse(f"PK: {pk}")