from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['username', 'rating', 'highest_rating','global_rank','country_rank']