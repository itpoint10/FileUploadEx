from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            #n1 = form.cleaned_data.get('fname')
            form.save()
            obj = form.instance
            return render(request, 'Resumes/home.html', {'form':form , 'obj':obj})
        else:
            return render(request, 'Resumes/home.html', {'form':form})
    else:
        msg = 'Please fill all the fields'
        return render(request, 'Resumes/home.html', { 'msg':msg})

def viewprofiles(request):
    if request.method == 'GET':
        rows = Profiles.objects.all()
        return render(request, 'Resumes/viewprofiles.html', {'rows':rows})

