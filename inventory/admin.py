from django.contrib import admin

from .models import Series, Film, User

# Register your models here.
admin.site.register(Series)
admin.site.register(Film)
admin.site.register(User)
