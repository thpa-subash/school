from django.contrib import admin
from .models import inbox
from .models import blog

# Register your models here.

admin.site.register(inbox)
admin.site.register(blog)
