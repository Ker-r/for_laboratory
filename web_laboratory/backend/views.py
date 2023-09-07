from django.shortcuts import render
from .models import Staff, Project


# Стартовая страница
def home(request):
    return render(request, 'web_laboratory/home.html')


def projects(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'web_laboratory/projects.html', context)


def staff(request):
    staffer = Staff.objects.all()
    context = {
        'staffer': staffer,
    }
    return render(request, 'web_laboratory/staff.html', context)
