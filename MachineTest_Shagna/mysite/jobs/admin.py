# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Registrationtbl)


admin.site.register(Venue)

admin.site.register(Score)

admin.site.register(Fixture)
