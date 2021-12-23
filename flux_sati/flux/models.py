from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Project Name")
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name="project description")
    start_year = models.CharField(max_length=10, null=True, blank=True, verbose_name="project start year")
    category = models.CharField(max_length=50, null=True, blank=True, verbose_name="project category")
    image1 = models.ImageField(upload_to='media', blank=True, null=True, default='')
    image2 = models.ImageField(upload_to='media', blank=True, null=True, default='')
    image3 = models.ImageField(upload_to='media', blank=True, null=True, default='')
    completed = models.BooleanField(null=False, blank=False, default=False, verbose_name="Is this project compleated")
    team = models.TextField(null=True, blank=True, default='[]', verbose_name='Team members')
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects" 

class Events(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Event Name")           
    organizer = models.CharField(max_length=50, blank=False, null=False, default='CLUB FLUX', verbose_name="Event Organizer")
    team = models.TextField(null=True, blank=True, default='[]', verbose_name='Team members')
    poster = models.ImageField(upload_to='media', blank=True, null=True, default='')
    faculty = models.TextField(null=True, blank=True, default='[]', verbose_name='Faculty members')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Events" 

class Registraion(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Student Name")
    year = models.CharField(max_length=10, blank=False, null=False)
    branch = models.CharField(max_length=50, blank=False, null=False)
    scholar_no = models.CharField(max_length=10, blank=True, null=True)
    enrollment_no = models.CharField(max_length=20, blank=True, null=True)
    contact_no = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "All Registrations"

class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Member Name")
    scholar_no = models.CharField(max_length=10, blank=True, null=True)
    enrollment_no = models.CharField(max_length=20, blank=True, null=True)
    contact_no = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
            return self.name

    class Meta:
        verbose_name_plural = "Team Members"    

class Gallery(models.Model):
    heading = models.CharField(max_length=50, blank=False, null=False, verbose_name="Image heading")   
    description = models.CharField(max_length=100, blank=False, null=False, verbose_name="Image description")
    image = models.ImageField(upload_to='media', blank=False, null=False, default='')      