from django.urls import path
from app import views

app_name='app'

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),

    path('nodes', views.nodes, name='nodes'),
    path('nodes_detail/<int:id>/',views.nodes_detail,name='nodes_detail'),

    path('sensors', views.sensors, name='sensors'),

]
