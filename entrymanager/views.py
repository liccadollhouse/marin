from django.db.models import F, Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django_tables2 import SingleTableView, MultiTableMixin

from .tables import EntryTable, EntryTableDivision
from .forms import ContestantEntryForm

from .models import ContestEntry, JudgingSlot, Division

# Create your views here.

def index(request):
     return render(request, 'index.html')


def contestantentry(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContestantEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():            
            # process the data in form.cleaned_data as required            
            try:
                judging_object = JudgingSlot.objects.get(judging_time="none")    
            except JudgingSlot.DoesNotExist:
                judging_object = JudgingSlot(judging_time="none")
                judging_object.save()
                
            divisionkey = form.cleaned_data['division']                   
            try:
                division_object = Division.objects.get(division_name=divisionkey)    
            except Division.DoesNotExist:
                division_object = Division(division_name=divisionkey)
                division_object.save()    
                
            ContestEntry.objects.create(
                legal_name = form.cleaned_data['legal_name'],
                cosplay_name = form.cleaned_data['cosplay_name'],
                character = form.cleaned_data['character'],
                series = form.cleaned_data['series'],
                google_entry_number = 0,
                email_address = form.cleaned_data['email_address'],
                division = division_object,
                judging_time = judging_object,
            )    
            # redirect to a new URL:
            return HttpResponseRedirect("/entrymanager/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContestantEntryForm()

    return render(request, "contestantentry.html", {"form": form})

def thanks(request):
    return render(request, 'thanks.html')

class AllEntriesView(SingleTableView):
    template_name = "allentries.html"
    model = ContestEntry
    table_class = EntryTable
    table_pagination = False 
    def get_table_kwargs(self):
        return {
            'order_by': ('cosplay_name')
        }
    
    
class EntryDetailView(generic.UpdateView):    
    template_name = "entrydetail.html"
    model = ContestEntry
    fields = ["cosplay_name","character","series","division","judging_time"]
    success_url = "/entrymanager/allentries"
    def form_valid(self, form):        
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.        
        divisionkey = form.cleaned_data['division']                   
        try:
            division_object = Division.objects.get(division_name=divisionkey)    
        except Division.DoesNotExist:
            division_object = Division(division_name=divisionkey)
            division_object.save()    
        
        division_index = list(dict(Division.VALID_DIVISIONS).values()).index(str(divisionkey))        
        TempEntry = ContestEntry.objects.get(cosplay_name=form.cleaned_data['cosplay_name'])
        if TempEntry.internal_division_number == 0:
            TempEntry.internal_division_number = ContestEntry.objects.filter(internal_division_number__gt=0,division=division_index).count() + 1
            TempEntry.save()
        
        return HttpResponseRedirect("/entrymanager/allentries/")

class EntriesByDivisionView(MultiTableMixin, generic.TemplateView):
    template_name = "entrybydivision.html"
    tables = [
            EntryTableDivision(ContestEntry.objects.filter(internal_division_number__gt=0,division=0),order_by='internal_division_number'),
            EntryTableDivision(ContestEntry.objects.filter(internal_division_number__gt=0,division=1),order_by='internal_division_number'),
            EntryTableDivision(ContestEntry.objects.filter(internal_division_number__gt=0,division=2),order_by='internal_division_number'),
            EntryTableDivision(ContestEntry.objects.filter(internal_division_number__gt=0,division=3),order_by='internal_division_number'),
            EntryTableDivision(ContestEntry.objects.filter(internal_division_number__gt=0,division=4),order_by='internal_division_number'),
            EntryTableDivision(ContestEntry.objects.filter(internal_division_number__gt=0,division=5),order_by='internal_division_number'),
    ]
    
