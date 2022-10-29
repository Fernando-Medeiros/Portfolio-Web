from django.db import models
from django.utils import timezone


STACKS_CATEGORY = (
    ('BACKEND', 'Back-end'),
    ('FRONTEND', 'Front-end'),
    ('DATABASE', 'Database'),
    ('FRAMEWORK', 'Framework'),
    ('CLOUD', 'Cloud'),
    ('LIBS', 'libraries'),
    ('TOOL', 'Tool'),
)


class Project(models.Model):
    title = models.CharField(max_length=100)
    template = models.ImageField(upload_to='project_templates')
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    link = models.URLField()
    github = models.URLField()

    def __str__(self) -> str:
        return self.title.title()



class ProjectDetail(models.Model):
    project = models.ForeignKey("Project", related_name="detail", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='thumb', default='')
    gif = models.ImageField(upload_to='thumb', default='')
    video = models.URLField()

    def __str__(self) -> str:
        return self.title.title()



class Stack(models.Model):
    projects = models.ManyToManyField('Project', related_name='stack')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icon_stack')
    category = models.CharField(max_length=100, choices=STACKS_CATEGORY)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name.title()