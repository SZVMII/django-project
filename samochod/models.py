from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _


class Part(models.Model):
    enumBodyType = [('sedan', 'Sedan'), ('kombi', 'Kombi'), ('hatchback', 'Hatchback'), ('cabriolet', 'Kabriolet'),
                    ('coupe', 'Coupe'), ]
    enumStatus = [('oczekujace', 'Oczekujące'), ('zaakceptowane', 'Zaakceptowane'), ('odrzucone', 'Odrzucone')]
    model = models.CharField(max_length=255, null=True)
    mark = models.CharField(max_length=255, null=True)
    startOfProduction = models.IntegerField(null=True)
    endOfProduction = models.IntegerField(null=True)
    engines = models.CharField(max_length=255, null=True)
    bodyType = models.CharField(max_length=255, choices=enumBodyType, default='sedan')
    partName = models.CharField(max_length=255)
    partOpis = models.CharField(max_length=1000)
    user_added = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=enumStatus, default='oczekujace')
