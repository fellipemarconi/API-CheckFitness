from django.contrib import admin
from .models import Personal, Student, Sport

# Register your models here.
@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username','name', 
        'is_personal', 'email'
    )
    search_fields = ('id', 'username', 'name', 'email')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'name', 'email', 'student_personal'
    )
    search_fields = ('id', 'username', 'name', 'email')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100
    
@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')