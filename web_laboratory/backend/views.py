from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Staff, Project


# Стартовая страница
def home(request):
    ''' Главная страница '''
    last_project = Project.objects.order_by('-pub_date')[:3]
    staff = Staff.objects.all()
    context = {
        'staff': staff,
        'last_project': last_project,
    }
    return render(request, 'web_laboratory/home.html', context)


class ProjectView(ListView):
    ''' Страница проектов '''
    paginate_by = 3
    model = Project
    template_name = 'web_laboratory/projects.html'
    context_object_name = 'project'


class ProjectDetail(DetailView):
    ''' Страница отдельного проекта '''
    model = Project
    template_name = 'web_laboratory/project_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_pk'


class StaffView(ListView):
    ''' Страница сотрудников '''
    paginate_by = 3
    model = Staff
    template_name = 'web_laboratory/staff.html'
    context_object_name = 'staffer'


class StaffDetail(DetailView):
    ''' Страница отдельного сотрудника '''
    model = Staff
    template_name = 'web_laboratory/staff_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_pk'
