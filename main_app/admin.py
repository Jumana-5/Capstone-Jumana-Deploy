from django.contrib import admin
from .models import item, category

# Register your models here.
# Admin name: Super1
# Admin password: garage123
# Admin email: super1@super.com



admin.site.register(item)
admin.site.register(category)

