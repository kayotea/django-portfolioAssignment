# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def test(request):
    return render(request, 'first_app/testimonials.html')

def projects(request):
    return render(request, 'first_app/projects.html')

def about(request):
    return render(request, 'first_app/about.html')