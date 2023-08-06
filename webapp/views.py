from django.shortcuts import render
from django.http import HttpResponse


def home(reuqest):
    return HttpResponse('Hey man!')
