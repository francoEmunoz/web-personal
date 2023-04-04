from django.shortcuts import render
from .models import Description

def about(request):
    description= Description.objects.all()
    return render(request, 'about/about.html', {'description': description})