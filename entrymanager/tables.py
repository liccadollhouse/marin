import django_tables2 as tables
from .models import ContestEntry
from django.db.models.functions import Lower, Upper

class EntryTable(tables.Table):
    cosplay_name = tables.Column(linkify=True)
    character = tables.Column(orderable=False)
    series = tables.Column(orderable=False)
    division = tables.Column(orderable=False)
    judging_time = tables.Column(orderable=False)    
    internal_division_number = tables.Column(orderable=False)
        
    def order_cosplay_name(self, queryset, is_descending):
        queryset = queryset.order_by(Lower("cosplay_name"))
        return (queryset, True)
    class Meta:
        model = ContestEntry
        template_name = "django_tables2/bootstrap.html"
        fields = ("cosplay_name", "character", "series", "division", "internal_division_number", "judging_time")
        
class EntryTableDivision(EntryTable):
    cosplay_name = tables.Column(linkify=True,orderable=False)
    internal_division_number = tables.Column(orderable=True)
    class Meta:
        model = ContestEntry
        template_name = "django_tables2/bootstrap.html"
        fields = ("cosplay_name", "character", "series", "division", "internal_division_number", "judging_time")
