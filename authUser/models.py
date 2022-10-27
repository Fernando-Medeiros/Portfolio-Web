from django.db import models
from django.contrib.auth.models import AbstractUser



class UserModel(AbstractUser):

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)