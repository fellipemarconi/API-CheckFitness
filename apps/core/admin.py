from django.contrib import admin
from .models import Personal

# Register your models here.
@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'is_personal',
        'first_name', 'last_name', 'email'
                    )
    search_fields = ('id', 'username', 'email')
    ordering = '-id',
    list_per_page = 25
    list_max_show_all = 100