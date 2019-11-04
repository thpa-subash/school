from django.contrib import admin

from .models import Services
from .models import teacher_detail
#
admin.site.register(teacher_detail)
admin.site.register(Services)


# Register your models here.
