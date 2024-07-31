from django.contrib import admin

from .models import Division, ContestEntry, JudgingSlot, HallContestEntry

# Register your models here.


class EntryInline(admin.TabularInline):
    model = ContestEntry
    extra = 2
    
class JudgingSlotInline(admin.TabularInline):
    model = ContestEntry
    extra = 2    
    
class DivisionAdmin(admin.ModelAdmin):   
    inlines = [EntryInline]
    list_filter = ["internal_division_number"]
class ContestEntryAdmin(admin.ModelAdmin):
    list_display = ["google_entry_number", "email_address","cosplay_name", "character", "series", "division", "internal_division_number", "judging_time"]
    list_filter = ["internal_division_number"]
class JudgingSlotAdmin(admin.ModelAdmin):
    inlines = [JudgingSlotInline]
    
class HallContestEntryAdmin(admin.ModelAdmin):    
    list_display = ["phone_number", "email_address","cosplay_name", "character", "series", "division"]  
      
admin.site.register(Division, DivisionAdmin)
admin.site.register(ContestEntry, ContestEntryAdmin)
admin.site.register(JudgingSlot, JudgingSlotAdmin)
admin.site.register(HallContestEntry, HallContestEntryAdmin)
