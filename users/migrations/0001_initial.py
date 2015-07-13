# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('invite', models.DateTimeField(auto_now=True)),
                ('accept', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Amigo',
                'verbose_name_plural': 'Amigos',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Rede Social',
                'verbose_name_plural': 'Redes Sociais',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255, null=True, blank=True)),
                ('company', models.CharField(max_length=255, null=True, blank=True)),
                ('avatar', models.TextField(null=True, blank=True)),
                ('cover', models.CharField(max_length=255)),
                ('phone_number_1', models.CharField(max_length=255)),
                ('phone_number_1_carrier', models.CharField(max_length=255)),
                ('phone_number_2', models.CharField(max_length=255, null=True, blank=True)),
                ('phone_number_2_carrier', models.CharField(max_length=255, null=True, blank=True)),
                ('website', models.CharField(max_length=255, null=True, blank=True)),
                ('street', models.CharField(max_length=255, null=True, blank=True)),
                ('neightborhood', models.CharField(max_length=255, null=True, blank=True)),
                ('city_state', models.CharField(max_length=255, null=True, blank=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='user',
            field=models.ForeignKey(to='users.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='id_owner',
            field=models.ForeignKey(related_name='id_owner', to='users.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='id_user',
            field=models.ForeignKey(related_name='id_user', to='users.User'),
        ),
    ]
