import csv

from django.core.management.base import BaseCommand, CommandError
from entrymanager.models import ContestEntry, Division, JudgingSlot

class Command(BaseCommand):
    help = "Imports the CSV used by AnimeFest from the Google Form."

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            googleentrynumber=0;
            try:
                judging_object = JudgingSlot.objects.get(judging_time="none")    
            except JudgingSlot.DoesNotExist:
                judging_object = JudgingSlot(judging_time="none")
                judging_object.save()
            for row in reader:
                if row[0] != "Timestamp" :
                    googleentrynumber = googleentrynumber + 1
                    divisionkey = "none"
                    
                    if row[12] == "Skits (craftsmanship judging optional)" :
                        divisionkey = "skit"
                    elif row[12] == "Masters" :
                        divisionkey = "master"
                    else :
                        divisionkey = row[12].lower()
                                        
                    try:
                        division_object = Division.objects.get(division_name=divisionkey)    
                    except Division.DoesNotExist:
                        division_object = Division(division_name=divisionkey)
                        division_object.save()                                        
                    
                    ContestEntry.objects.create(
                        legal_name = row[2].strip(),
                        cosplay_name = row[3].strip(),
                        character = row[6].strip(),
                        series = row[7].strip(),
                        google_entry_number = googleentrynumber,
                        email_address = row[1].strip(),
                        division = division_object,
                        judging_time = judging_object
                    )
                    

