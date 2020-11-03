from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bath', views.bath, name='bath')
]