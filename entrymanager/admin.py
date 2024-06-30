from django.contrib import admin

from .models import Division, ContestEntry

# Register your models here.


class EntryInline(admin.TabularInline):
    model = ContestEntry
    extra = 5
    
class DivisionAdmin(admin.ModelAdmin):   
    inlines = [EntryInline]
    
admin.site.register(Division, DivisionAdmin)
