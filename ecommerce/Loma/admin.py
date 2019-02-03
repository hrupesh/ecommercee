# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import promocode_model, Loma_master, Loma_operation_model, Daily_price_list, approved_pl_by_loma, MD_model, loma_attendance_model
from django.contrib import admin

# Register your models here.

admin.site.register(promocode_model)

admin.site.register(Loma_master)

admin.site.register(Loma_operation_model)

admin.site.register(Daily_price_list)

admin.site.register(approved_pl_by_loma)

admin.site.register(loma_attendance_model)

admin.site.register(MD_model)