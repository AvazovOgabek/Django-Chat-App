# Generated by Django 5.0 on 2023-12-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='message_images'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
