from unicodedata import category
from .models import Project, Stack


def all_projects(request):
    projects = Project.objects.all().order_by('-created_at')
    
    if projects == None or projects == '':
        return {'allProjects': ''}

    return {'allProjects': projects}


def all_stacks(request):
    stacks = Stack.objects.all().order_by('created_at')
    
    if stacks == None or stacks == '':
        return {'allStacks': ''}

    return {'allStacks': stacks}