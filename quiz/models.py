from django.db import models
from questions import *
import random
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text='Testni vaqtini kiriting: ')
    required_score_to_pass = models.IntegerField(help_text='natija')

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name = 'Ro\'yxat'
        verbose_name_plural = 'Savollar ro\'yxati'