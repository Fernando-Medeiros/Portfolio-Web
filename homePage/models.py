from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb')
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    link = models.URLField()
    github = models.URLField()

    def __str__(self) -> str:
        return self.title.title()



class ProjectDetail(models.Model):
    project = models.ForeignKey("Project", related_name="detail", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    thumb1 = models.ImageField(upload_to='thumb', default='')
    thumb2 = models.ImageField(upload_to='thumb', default='')
    video = models.URLField()

    def __str__(self) -> str:
        return self.title.title()