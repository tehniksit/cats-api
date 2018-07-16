#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Cat(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Имя')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    breed = models.CharField(max_length=255, verbose_name='Порода')
    color = models.CharField(max_length=255, verbose_name='Окрас')

    def __str__(self):
        return (str(self.pk)+ " " + str(self.name))

    def get_pk(self):
        	return(self.pk)  