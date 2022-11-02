from django.urls import path

from .views import HomePage

app_name = 'homePage'


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]