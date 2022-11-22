from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Course, Experience, Formation, UserDetail, UserModel

admin.site.register(UserModel, UserAdmin)
admin.site.register(UserDetail)
admin.site.register(Formation)
admin.site.register(Course)
admin.site.register(Experience)