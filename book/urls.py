from django.urls import path

# import all book views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
