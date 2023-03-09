from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutUs'),
    path('browseJobs/', views.browseJobs, name='browseJobs'),
    path('profile/employer/', views.employer, name='employer'),
    path('profile/freelancer/', views.freelancer, name='freelancer'),
    path('howItWorks/', views.howItWorks, name='howItWorks'),
    path('logIn/', views.logIn, name='logIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('profile/freelancer/report/', views.reportFreelancer, name='reportFreelancer'),
    path('profile/employer/report/', views.reportEmoloyer, name='reportEmployer'),
    path('profile/', views.profile, name='profile'),

]