from django.contrib import admin
from .models import NSManufacturer, NSShoeType, NSShoeColor, NSShoe

admin.site.register(NSManufacturer)
admin.site.register(NSShoeType)
admin.site.register(NSShoeColor)
admin.site.register(NSShoe)
