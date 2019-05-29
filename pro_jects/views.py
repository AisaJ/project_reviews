from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import NewProfileForm,NewProjectForm
# Create your views here.

def home(request):
  projects=Project.objects.all()
  return render(request,'home.html',{"projects":projects})

@login_required(login_url='/accounts/login')
def new_profile(request):
  current_user=request.user
  if request.method == 'POST':
    form=NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      prof_pic=form.cleaned_data['prof_pic']
      bio=form.cleaned_data['bio']
      contact = form.cleaned_data['contact']
      Profile.objects.filter(user=current_user).update(bio=bio,prof_pic=prof_pic,contact=contact)
      profile.save()

    return redirect('profile') 
  else:
    form = NewProfileForm()
  return render(request,'new-profile htm',{"form":form})

@login_required(login_url='/accounts/login')
def project_add(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewProjectForm(request.POST,request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.user = current_user
      project.save()
    return redirect('home')

  else:
    form=NewProjectForm()
    return render(request,'project-add.html',{'form':form})