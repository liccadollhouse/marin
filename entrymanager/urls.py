from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contestantentry/", views.contestantentry, name="contestantentry"),
    path("thanks/", views.thanks, name="thanks"),
    path("allentries/", views.AllEntriesView.as_view(), name="allentries"),
    path("<int:pk>/", views.EntryDetailView.as_view(), name="detail"),
    path("entriesbydivision/", views.EntriesByDivisionView.as_view(), name="entriesbydivision"),
] 
