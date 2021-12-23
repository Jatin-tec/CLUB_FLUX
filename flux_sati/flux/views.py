from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    compleate_projects = Projects.objects.filter(completed=True)
    ongoing_projects = Projects.objects.filter(completed=False)
    projects = Projects.objects.all() 

    return render(request, 'index.html', {'projects' : projects, 'compleate_projects' : compleate_projects, 'ongoing_projects' : ongoing_projects})

def project_desc(request, id=""):
    project = Projects.objects.get(id=id)

    return render(request, 'project-details.html', {'project' : project})    

def registration_form(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        email = request.POST.get('email')
        scholar_number = request.POST.get('scholar_number')
        enrollment_number = request.POST.get('enrollment_number')
        phone_number = request.POST.get('phone_number')

        event = Events.objects.filter()[0]
        student = Registraion()
        student.event = event
        student.name = name
        student.year = year
        student.branch = branch
        student.email = email
        student.scholar_no = scholar_number
        student.enrollment_no = enrollment_number
        student.contact_no = phone_number

        student.save()        

    return render(request, 'event_registration_form.html')    