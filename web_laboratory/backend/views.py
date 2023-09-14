from django.shortcuts import get_object_or_404, render
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


def project_detail(request, project_id):
    post = get_object_or_404(Project, pk=project_id)
    context = {
        'post': post,
    }
    return render(request, 'web_laboratory/project_detail.html', context)
