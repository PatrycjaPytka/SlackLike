from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .forms import NewGroupForm, FindGroupform
from .models import Groups


def index(request):
    group_names = Groups.objects.all()
    who_ask = request.user
    form = FindGroupform()

    return  render(request, 'chat_main/index.html', {
                'group_names': group_names,
                'who_ask': who_ask,
                'form': form,
                })


def room(request, room_name):
    group_names = Groups.objects.all()
    users = Groups.objects.get(name_of_group=room_name)
    who_ask = request.user
    return render(request, 'chat_main/room.html', {
                'room_name': room_name,
                'group_names': group_names,
                'users': users,
                'who_ask': who_ask,
                })


def new_group(request):
    form_group = NewGroupForm(request.POST or None)

    if request.method == 'POST':
        form_group.save()

    if form_group.is_valid():   
        form_group.save()
        return(redirect('chat_main:index'))

    else:
        form_group = NewGroupForm()

    return render(request, 'chat_main/new_group.html', {
                'form_group': form_group, 
                'new': True,
                })


def edit_group(request, room_name):
    group = Groups.objects.get(name_of_group=room_name)
    form_group = NewGroupForm(request.POST or None, instance=group)

    if request.method == 'POST':
        form_group.save()

    if form_group.is_valid():   
        form_group.save()
        return(redirect('chat_main:index'))
    
    return render(request, 'chat_main/new_group.html', {
                'form_group': form_group, 
                'new': False,
                })


def delete_group(request):
    groups = Groups.objects.all()
    return render(request, 'chat_main/delete_group.html', {
                'groups': groups,
                })


def confirm(request, group):
    to_delete = Groups.objects.get(name_of_group=group)
    
    if request.method == 'POST':
        to_delete.delete()
        return redirect('chat_main:index')

    return render(request, 'chat_main/confirm.html', {
                'to_delete': to_delete,
                'leave': False,
                })


def leave_group(request, group):
    to_delete = Groups.objects.get(name_of_group=group)
    user = request.user

    if request.method == 'POST':
        to_delete.members.remove(user)
        return redirect('chat_main:index')

    return render(request, 'chat_main/confirm.html', {
                'to_delete': to_delete,
                'leave': True,
                'user': user,
                })


def find_group(request):
    if request.method == 'GET':
        try:
            group = Groups.objects.get(name_of_group=request.GET['name_of_group'])

            return redirect('chat_main:room', group)

        except Groups.DoesNotExist:
            
            return HttpResponse('Group does not exist')

        else:
            return HttpResponse('Something went wrong')
