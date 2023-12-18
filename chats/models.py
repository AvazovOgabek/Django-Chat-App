from django.db import models
from profiles.models import Profile


class Chat(models.Model):
    person = models.ForeignKey(Profile, related_name='chats_as_person', on_delete=models.CASCADE) 
    you = models.ForeignKey(Profile, related_name='chats_as_you', on_delete=models.CASCADE)

class Message(models.Model):
    profile = models.ForeignKey(Profile, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)  # For text messages
    image = models.ImageField(upload_to='message_images', blank=True, null=True)  

    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)