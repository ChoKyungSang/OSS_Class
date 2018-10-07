# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule
from django.utils import timezone


def post_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'blog/post_list.html',  {'schedules': schedules})