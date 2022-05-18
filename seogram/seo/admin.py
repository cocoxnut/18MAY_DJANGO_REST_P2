from django.contrib import admin

from .models import Pricing, Blog, Category

admin.site.register(Pricing)
admin.site.register(Blog)
admin.site.register(Category)

# Register your models here.
