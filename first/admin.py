from django.contrib import admin

# Register your models here.
from first.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

