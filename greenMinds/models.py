from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE) # delete the profile if the user deletes his/her account
    rate = models.FloatField()
    completedJobs = models.IntegerField()
    joinedDate = models.DateTimeField(default=timezone.now)
    #skills = 
    about = models.TextField()
    #certifications =
    wallet = models.FloatField()

    def __str__(self) -> str:
        return self.username.username
