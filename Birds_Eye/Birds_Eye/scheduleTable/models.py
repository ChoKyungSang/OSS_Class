# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Schedule(models.Model):
    name = models.CharField(max_length=20)
    division = models.IntegerField(default=1)
    locate = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    prof = models.CharField(max_length=15)
    
    def __str__(self): #추가된 스케줄 객체를 표시할떄 사용할 스트링을 name 필드로 변경해주는 함수 
        return self.name
# Create your models here.
