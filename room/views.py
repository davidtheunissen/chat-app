from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {
        'rooms': rooms
    })


@login_required
def room(request, room_name):
    room = Room.objects.get(slug=room_name)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {
        'room': room,
        'messages': messages,
    }) 