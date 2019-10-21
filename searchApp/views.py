from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the search engine.")


def results(request):
    response = "You're looking at the results of query ___"
    return HttpResponse(response)
