from .models import Project


def all_projects(request):
    projects = Project.objects.all().order_by('-created_at')
    
    if projects == None or projects == '':
        return {'allProjects': ''}

    return {'allProjects': projects}