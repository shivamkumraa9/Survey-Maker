from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class User_survey(models.Model):
    auther=models.ForeignKey(User, on_delete=models.CASCADE)
    heading=models.CharField(max_length=45)
    total_filled=models.IntegerField(default=0)

    def __str__(self):
        return self.heading


class Question(models.Model):
    part=models.ForeignKey(User_survey, on_delete=models.CASCADE)
    text=models.CharField(max_length=60)
    def __str__(self):
        return self.text

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    text=models.CharField(max_length=30)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.text

class Fillers(models.Model):
    users_filled=models.ManyToManyField(User)
    survey=models.OneToOneField(User_survey,on_delete=models.CASCADE)

    def __str__(self):
        return "{} --> ".format(self.survey.heading)

