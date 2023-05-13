from django.shortcuts import render
from .models import Description
from django.http.response import HttpResponse
import mimetypes
import os

def about(request):
    description= Description.objects.all()
    return render(request, 'about/about.html', {'description': description})

def descargar_archivo(request): 
 
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
 
    filename = 'Franco_Muñoz_CV.pdf'
 
    filepath = BASE_DIR + '/about/descargar/' + filename
 
    path = open(filepath, 'rb')
 
    mime_type, _ = mimetypes.guess_type(filepath)
    
    response = HttpResponse(path, content_type = mime_type)
 
    response['Content-Disposition'] = f"attachment; filename={filename}"
 
    return response