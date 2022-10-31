# Generated by Django 4.1.2 on 2022-10-30 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0008_project_user'),
        ('authUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='profile_images')),
                ('about', models.TextField(max_length=2000)),
                ('website', models.URLField()),
                ('linkedin', models.URLField()),
                ('youtube', models.URLField()),
                ('github', models.URLField()),
                ('projects', models.ManyToManyField(related_name='project', to='homePage.project')),
                ('stacks', models.ManyToManyField(related_name='stack', to='homePage.stack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
