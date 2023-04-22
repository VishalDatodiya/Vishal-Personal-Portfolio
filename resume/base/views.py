from django.shortcuts import render

from base.models import Project

def home(request):
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    return render(request, 'base/index.html', context)
