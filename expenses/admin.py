from django.contrib import admin

from . import models

admin.site.register(models.Account)
admin.site.register(models.Expense)
admin.site.register(models.Budget)
