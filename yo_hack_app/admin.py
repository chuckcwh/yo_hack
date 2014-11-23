from django.contrib import admin

# Register your models here.
from yo_hack_app.models import Profile, Action, Family

admin.site.register(Profile)
admin.site.register(Family)
admin.site.register(Action)