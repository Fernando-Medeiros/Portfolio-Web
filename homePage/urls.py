from django.urls import path
from .views import home


app_name = 'homePage'


urlpatterns = [
    path('', home, name='home'),
]