import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
from haikunator import Haikunator
from .models import Room

# Create your views here.

def about(request):
        return render(request, "chat/aout.html")

def new_room(request):
        new_room = None
        while not new_room:
                with transaction.atomic():
                        label = Haikunator.haikunate()
                        if Room.objects.filter(label=label).exists():
                                continue
                        new_room = Room.objects.create(label=label)
        return redirect(chat_room, label=label)

def chat_room(request, label):
        room, created = Room.objects.get_or_create(label=label)

        messages = reversed(room.messages.order_by('-timestamp')[:50])

        return render(request, "chat/room.html", {
        'room':room,
        'message': messages,
})
