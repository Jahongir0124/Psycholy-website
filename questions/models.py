from django.db import models
from quiz.models import Quiz
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
class Question(models.Model):
    text = models.CharField(max_length=1000)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        verbose_name = 'Savol'
        verbose_name_plural = 'Savollar'

class Answer(models.Model):
    text = models.CharField(max_length=900)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"questions:{self.question.text},answer : {self.text},correct:{self.correct}"


    class Meta:
        verbose_name = 'Javob'
        verbose_name_plural = 'Javoblar'