from django.urls import path, re_path
from app import views



urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
