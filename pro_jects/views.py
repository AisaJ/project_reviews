from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  render(request,'home.html')