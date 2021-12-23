from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    compleate_projects = Projects.objects.filter(completed=True)
    ongoing_projects = Projects.objects.filter(completed=False)
    
    # projects = 

    print(compleate_projects)

    return render(request, 'index.html', {'compleate_projects' : compleate_projects, 'ongoing_projects' : ongoing_projects})