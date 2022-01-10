from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Psychologist(models.Model):
    user = models.OneToOneField(User,verbose_name='Foydalanuvchi',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='FIO')
    phone_number = models.CharField(max_length=100,verbose_name='Telefon nomer')
    resume = models.FileField()
    image = models.ImageField()
    specialist = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    class Meta:
        verbose_name = _('Psixolog')
        verbose_name_plural = _('Psixologlar')

    def __str__(self):
        return self.name
class Projects(models.Model):
     author = models.ForeignKey(Psychologist,on_delete=models.CASCADE)
     name = models.CharField(max_length=200,null=False)
     description = models.CharField(max_length=150,null=True)
     text = models.TextField()
     image = models.ImageField()
     file = models.FileField()

     class Meta:
         verbose_name = _('Maqola')
         verbose_name_plural = _('Maqolalar')


