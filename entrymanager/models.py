from django.db import models


# Create your models here.
  
class JudgingSlot(models.Model):
    VALID_JUDGING_TIMES = [
        ("none","Not Assigned"),
        ("skitonly","Skit Entry With No Prejudging"),
        ("exhibition","Strut Your Stuff"),
        ("072613001400","Friday, July 26th, 1pm-2pm"),
        ("072614001500","Friday, July 26th, 2pm-3pm"),
        ("072615001600","Friday, July 26th, 3pm-4pm"),
        ("072616001700","Friday, July 26th, 4pm-5pm"),
        ("072617001800","Friday, July 26th, 5pm-6pm"),
        ("072710001100","Saturday, July 27th, 10am-11am"),
        ("072711001200","Saturday, July 27th, 11am-12pm"),
        ("072713001400","Saturday, July 27th, 1pm-2pm"),
        ("072714001500","Saturday, July 27th, 2pm-3pm"),         
    ]
    judging_time = models.CharField(max_length=50,choices=VALID_JUDGING_TIMES,default="none")  
    def __str__(self):
        return self.get_judging_time_display()

class Division(models.Model):
    VALID_DIVISIONS = [
        ("youth","Youth"),
        ("novice","Novice"),
        ("journeyman","Journeyman"),
        ("master","Master"),
        ("skit","Skit"),
        ("exhibition","Strut Your Stuff"), # AnimeFest/GameFest has an exhibition division called "Strut Your Stuff".
    ]
    division_name = models.CharField(max_length=50,choices=VALID_DIVISIONS,default="novice")
    def __str__(self):
        return self.get_division_name_display()

class ContestEntry(models.Model): 
    legal_name = models.CharField(max_length=50)
    cosplay_name = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=15,default="Unknown")
    character = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    judging_time = models.ForeignKey(JudgingSlot,on_delete=models.CASCADE) 
    division = models.ForeignKey(Division,on_delete=models.CASCADE)    
    google_entry_number = models.IntegerField(default=-1)
    email_address = models.CharField(max_length=50)
    internal_division_number = models.IntegerField(default=0)    
    def __str__(self):
        return self.cosplay_name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("entrymanager:detail", kwargs={"pk": self.pk})
    
class HallContestEntry(models.Model):  
    VALID_DIVISIONS = [
        ("novice","Novice"),
        ("journeyman","Journeyman"),
        ("master","Master"),
    ]   
    legal_name = models.CharField(max_length=50)
    cosplay_name = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=15,default="Unknown")
    character = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    division = models.CharField(max_length=50,choices=VALID_DIVISIONS,default="novice")
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)    
    def __str__(self):
        return self.cosplay_name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("entrymanager:detailhall", kwargs={"pk": self.pk})    
    
    

