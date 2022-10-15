from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_diplay = ['title','unit_price']

admin.site.register(models.Collection)


admin.site.register(models.Product)
# admin.site.register(models.Collection)
# admin.site.register(models.Collection)
# admin.site.register(models.Collection)
# admin.site.register(models.Collection)

