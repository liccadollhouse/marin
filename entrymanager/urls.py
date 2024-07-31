from django.urls import path

from . import views

app_name = "entrymanager"
urlpatterns = [
    path("", views.index, name="index"),
    path("contestantentry/", views.contestantentry, name="contestantentry"),
    path("thanks/", views.thanks, name="thanks"),
    path("allentries/", views.AllEntriesView.as_view(), name="allentries"),
    path("<int:pk>/", views.EntryDetailView.as_view(), name="detail"),
    path("<int:pk>/badgesticker/", views.BadgeStickerView.as_view(), name="badgesticker"),
    path("entriesbydivision/", views.EntriesByDivisionView.as_view(), name="entriesbydivision"),
    path("managerview/", views.managerview, name="managerview"),
    path("allentriesjudging/", views.AllEntriesJudgingView.as_view(), name="allentriesjudging"),
    path("<int:pk>/judgingform/", views.EntryJudgingFormView.as_view(), name="judgingform"),
    path("hallcontestentry/", views.HallContestEntryView.as_view(), name="hallcontestentry"),
    path("thankshall/", views.thankshall, name="thankshall"),
    path("hallallentries/", views.HallAllEntriesView.as_view(), name="hallallentries"),
    path("<int:pk>/detailhall/", views.HallEntryDetailView.as_view(), name="detailhall"),
] 
