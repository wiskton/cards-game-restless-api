# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    #list_filter = ['ativo', ]
    #list_editable = ['ativo', ]
    #readonly_fields = ['cliques', ]
    save_on_top = True
    list_per_page = 20
    

admin.site.register(User, UserAdmin)