from django.contrib import admin

from .models import Division, ContestEntry, JudgingSlot

# Register your models here.


class EntryInline(admin.TabularInline):
    model = ContestEntry
    extra = 2
    
class JudgingSlotInline(admin.TabularInline):
    model = ContestEntry
    extra = 2    
    
class DivisionAdmin(admin.ModelAdmin):   
    inlines = [EntryInline]
    
class ContestEntryAdmin(admin.ModelAdmin):
    list_display = ["google_entry_number", "email_address","cosplay_name", "character", "series", "division", "internal_division_number", "judging_time"]
    
class JudgingSlotAdmin(admin.ModelAdmin):
    inlines = [JudgingSlotInline]
    
admin.site.register(Division, DivisionAdmin)
admin.site.register(ContestEntry, ContestEntryAdmin)
admin.site.register(JudgingSlot, JudgingSlotAdmin)
