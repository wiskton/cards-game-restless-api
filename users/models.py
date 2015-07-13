# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    profession = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.TextField(null=True, blank=True)
    cover = models.CharField(max_length=255)

    phone_number_1 = models.CharField(max_length=255)
    phone_number_1_carrier = models.CharField(max_length=255)
    phone_number_2 = models.CharField(max_length=255, null=True, blank=True)
    phone_number_2_carrier = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    street = models.CharField(max_length=255, null=True, blank=True)
    neightborhood = models.CharField(max_length=255, null=True, blank=True)
    city_state = models.CharField(max_length=255, null=True, blank=True)

    #QR Code #card://user/id/:32423432

    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'
        
    def __unicode__(self):
        return "%s" % self.email
        
class SocialNetwork(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = u'Rede Social'
        verbose_name_plural = u'Redes Sociais'
        
    def __unicode__(self):
        return "%s" % self.name
        

class Friend(models.Model):
    id_owner = models.ForeignKey(User, related_name='id_owner')
    id_user = models.ForeignKey(User, related_name='id_user')
    active = models.BooleanField(default=True)
    invite = models.DateTimeField(auto_now=True)
    accept = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = u'Amigo'
        verbose_name_plural = u'Amigos'
        
    def __unicode__(self):
        return "%s" % self.id_owner
        