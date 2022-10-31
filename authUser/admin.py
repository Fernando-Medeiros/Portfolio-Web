from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserModel, UserDetail, Formation, Course, Experience


admin.site.register(UserModel, UserAdmin)
admin.site.register(UserDetail)
admin.site.register(Formation)
admin.site.register(Course)
admin.site.register(Experience)