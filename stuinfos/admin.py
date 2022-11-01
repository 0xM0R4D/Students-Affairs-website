from django.contrib import admin

# Register your models here.
from .models import stu
from .models import course
from .models import coursestudent

admin.site.register(stu)
admin.site.register(course)
admin.site.register(coursestudent)
