from django.db import models
from django.utils.translation import ugettext_lazy as _

class Login(models.Model):
    username = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=False)

    class Meta:
        verbose_name = _('Login')

