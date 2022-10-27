from django.urls import path

from .views import HomePage, ProfilePage

app_name = 'homePage'


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('profile/', ProfilePage.as_view(), name='profile'),

]