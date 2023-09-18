from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from .models import Staff, Project


# Стартовая страница
def home(request):
    last_project = Project.objects.all()[:3]
    context = {
        'last_project': last_project,
    }
    return render(request, 'web_laboratory/home.html', context)


class ProjectView(ListView):
    model = Project
    template_name = 'web_laboratory/projects.html'
    context_object_name = 'project'

    # def get(self, request):
    #     project = Project.objects.all()
    #     context = {
    #         'project': project,
    #     }
    #     return render(request, 'web_laboratory/projects.html', context)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'web_laboratory/project_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_pk'


    # def get(self, request, pk):
    #     post = Project.objects.get(id=pk)
    #     context = {
    #         'post': post,
    #     }
    #     return render(request, 'web_laboratory/project_detail.html', context)


def staff(request):
    staffer = Staff.objects.all()
    context = {
        'staffer': staffer,
    }
    return render(request, 'web_laboratory/staff.html', context)
