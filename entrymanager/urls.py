from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contestantentry/", views.contestantentry, name="contestantentry"),
    path("thanks/", views.thanks, name="thanks"),
] 
