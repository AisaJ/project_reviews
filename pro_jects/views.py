from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
# Create your views here.

def home(request):
  projects=Project.objects.all()
  return render(request,'home.html',{"projects":projects})