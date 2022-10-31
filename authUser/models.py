from django.db import models
from django.contrib.auth.models import AbstractUser



class UserModel(AbstractUser):

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class UserDetail(models.Model):
    user = models.ForeignKey('UserModel', related_name='detail', on_delete=models.CASCADE)
    projects = models.ManyToManyField('homePage.Project', related_name='projects')
    stacks = models.ManyToManyField('homePage.Stack', related_name='stacks')
    photo = models.ImageField(upload_to='profile_images')
    about = models.TextField(max_length=2000)
    website = models.URLField()
    linkedin = models.URLField()
    youtube = models.URLField()
    github = models.URLField()

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Formation(models.Model):
    user = models.ForeignKey('UserModel', related_name='formation', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.name


class Course(models.Model):
    user = models.ForeignKey('UserModel', related_name='course', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    user = models.ForeignKey('UserModel', related_name='experience', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=2000)
    start = models.DateField()
    end = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.name