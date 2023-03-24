from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Freelancer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE) # delete the profile if the user deletes his/her account
    name = models.CharField(max_length=50)
    profilePic = models.ImageField(blank=True)
    email = models.EmailField()
    rate = models.FloatField(blank=True)
    completedJobs = models.IntegerField(blank=True)
    joinedDate = models.DateTimeField(default=timezone.now)
    skills = models.TextField(blank=True)
    about = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    wallet = models.FloatField(blank=True)

    def __str__(self) -> str:
        return f'{self.id} | {self.name}'
    

class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE) # delete the profile if the user deletes his/her account
    name = models.CharField(max_length=50) 
    profilePic = models.ImageField(blank=True)
    email = models.EmailField()
    about = models.TextField(blank=True)
    completedProjects = models.TextField(blank=True)
    availableProjects = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.id} | {self.name}'

