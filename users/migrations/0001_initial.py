# Generated by Django 4.2.5 on 2024-03-26 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=500, null=True)),
                ('short_intro', models.CharField(max_length=500, null=True)),
                ('bio', models.TextField(null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('social_github', models.CharField(max_length=200, null=True)),
                ('social_twitter', models.CharField(max_length=200, null=True)),
                ('social_linkedin', models.CharField(max_length=200, null=True)),
                ('social_website', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
