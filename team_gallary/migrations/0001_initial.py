# Generated by Django 5.0.1 on 2024-01-29 12:18

import team_gallary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img', models.ImageField(upload_to='gallery/', validators=[team_gallary.models.validate_image_size])),
                ('gallery_title', models.CharField(max_length=50)),
                ('gallery_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_img', models.ImageField(upload_to='team/', validators=[team_gallary.models.team_validate_image_size])),
                ('member_name', models.CharField(max_length=200)),
                ('member_title', models.CharField(max_length=200)),
                ('member_description', models.TextField()),
                ('linkedin_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('github_url', models.URLField()),
                ('website_url', models.URLField()),
            ],
        ),
    ]