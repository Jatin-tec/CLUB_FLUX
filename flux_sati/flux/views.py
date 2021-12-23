from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    compleate_projects = Projects.objects.filter(completed=True)
    ongoing_projects = Projects.objects.filter(completed=False)
    
    # projects = 

    return render(request, 'index.html', {'compleate_projects' : compleate_projects, 'ongoing_projects' : ongoing_projects})

def project_desc(request, id=""):
    project = Projects.objects.get(id=id)

    return render(request, 'project-details.html', {'project' : project})    