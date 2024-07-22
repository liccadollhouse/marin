from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import ContestantEntryForm

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
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/entrymanager/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContestantEntryForm()

    return render(request, "contestantentry.html", {"form": form})

def thanks(request):
    return render(request, 'thanks.html')
