from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from homepage.models import Room, Message
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import UserProfile


class Home(ListView):
    template_name = 'homepage/home.html'
    queryset = User.objects.all()


def create_room(request):
    user2 = request.POST.get('user2')
    user2 = User.objects.get(pk=user2)

    try:
        room = Room.objects.get(user1=request.user, user2=user2)

    except:

        try:
            room = Room.objects.get(user1=user2, user2=request.user)

        except:
            room = Room(user1=request.user, user2=user2)
            room.save()

    return HttpResponseRedirect(reverse('homepage:room_detail', args=(room.id,)))


def create_message(request, room_id):
    message = request.POST.get('message')
    room = Room.objects.get(pk=room_id)
    message = Message(text=message, user=request.user, room=room)
    message.save()
    return HttpResponseRedirect(reverse('homepage:room_detail', args=(room_id,)))


class RoomView(DetailView):
    template_name = 'homepage/room.html'
    model = Room
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=self.object)

        return context



class Detail(DetailView):
    template_name = 'homepage/detail.html'
    model = UserProfile
    context_object_name = 'user_object'



