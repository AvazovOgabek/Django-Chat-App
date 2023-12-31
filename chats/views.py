from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
from .models import Chat, Message

@login_required(login_url='signin')
def home(request):

    my_profile = Profile.objects.get(user=request.user)
    chats = Chat.objects.filter(Q(you=my_profile) | Q(person=my_profile))

    return render(request, 'home.html', {'my_profile' : my_profile, 'chats' : chats })

@login_required(login_url='signin')
def search(request):
    user = None
    if request.method == 'POST':
        username = request.POST.get('username')
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            profile = Profile.objects.get(user=user)
            return render(request, 'search.html', {'profile': profile})
        
        messages.error(request, 'Profile does not exist')
        return render(request, 'search.html', {'user': user})
    else:
        user = User.objects.none()
    return render(request, 'search.html', {'user': user})

@login_required(login_url='signin')
def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    
    if request.method == 'POST':
        you = get_object_or_404(Profile, user=request.user)
        
        chat_exists_1 = Chat.objects.filter(you=you, person=profile).exists()
        chat_exists_2 = Chat.objects.filter(you=profile, person=you).exists()

        
        if chat_exists_1 or chat_exists_2:
            chat = Chat.objects.get(you=you, person=profile)
            return redirect('chat', chat_id=chat.id)
        else:
            chat = Chat.objects.create(you=you, person=profile)
            chat.save()
            return redirect('chat', chat_id=chat.id)
    
    return render(request, 'profile_detail.html', {'profile': profile})

@login_required(login_url='signin')
def chat(request, chat_id):  
    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')

        profile = Profile.objects.get(user=request.user)
        chat = Chat.objects.get(pk=chat_id)

        message = Message(profile=profile, chat=chat, content=content)
        if image:
            message.image = image
        message.save()
        return redirect('chat', chat_id=chat_id)
    else:
        chat = get_object_or_404(Chat, id=chat_id)
        messages = Message.objects.filter(chat=chat)
        my_profile = Profile.objects.get(user=request.user)
        chats = Chat.objects.filter(Q(you=my_profile) | Q(person=my_profile))
        
        return render(request, 'chat.html', {'chat': chat, 'messages': messages, 'my_profile' : my_profile, 'chats' : chats, 'chat_id' : chat_id})

@login_required(login_url='signin')
def my_profile(request):
    proifle = Profile.objects.get(user=request.user)
    return render(request, 'my_profile.html', {'profile' : proifle})

@login_required(login_url='signin')
def delete_chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    chat.delete()
    return redirect('home')

@login_required(login_url='signin')
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        profile_image = request.FILES.get('profile_image')
        
        if profile_image:
            profile.profile_img = profile_image
        if bio:
            profile.bio = bio
        if last_name:
            profile.last_name = last_name
        if first_name:
            profile.first_name = first_name
        
        profile.save()
        return redirect('my_profile')  

    return render(request, 'edit_profile.html', {'profile': profile})

