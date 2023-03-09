from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='profile'),
    path('report/', views.report, name='report'),
]
