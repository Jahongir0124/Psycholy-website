from django.db import models
from quiz.models import Quiz
from questions.models import *
from django.contrib.auth.models import User
# Create your models here.


class Result(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk) +' '+ self.user.first_name +' '+ self.user.last_name

    class Meta:
        verbose_name = 'Natijalar'
        verbose_name_plural = 'Natijalar'