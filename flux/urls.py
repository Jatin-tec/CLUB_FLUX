from django.contrib import admin
from django.urls import path, include
from . import views as flux_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', flux_views.index, name='index'),
    path('project/<int:id>/', flux_views.project_desc, name='project_description'),
    path('registration/', flux_views.registration_form, name='registration'),
    path('subscribe/', flux_views.subscription, name='subscribe')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
