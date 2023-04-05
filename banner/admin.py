from django.contrib import admin
from .models import usersignup,mynotes,feedback

# Register your models here.
admin.site.register(usersignup)
admin.site.register(mynotes)
admin.site.register(feedback)