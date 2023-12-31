# Generated by Django 5.0 on 2023-12-18 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0002_remove_message_receiver_remove_message_sender_and_more'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chats_as_person', to='profiles.profile')),
                ('you', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_as_you', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ManyToManyField(to='chats.chat')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='profiles.profile')),
            ],
        ),
    ]
