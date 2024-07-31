from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django_tables2 import SingleTableView, MultiTableMixin

from .tables import EntryTable, EntryTableDivision
from .forms import ContestantEntryForm

from .models import ContestEntry, JudgingSlot, Division
from PIL import Image, ImageDraw, ImageFont

from brother_ql.devicedependent import models, label_sizes, label_type_specs, DIE_CUT_LABEL, ENDLESS_LABEL, ROUND_DIE_CUT_LABEL
from brother_ql.backends import available_backends, backend_factory

# We use this section to generate badge stickers.

size = (690, 600)
font_regular = ImageFont.truetype("FreeSansBold.ttf",40)
font_regular2 = ImageFont.truetype("FreeSansBold.ttf",40)
font_regular3 = ImageFont.truetype("FreeSansBold.ttf",45)
font_judgingtime = ImageFont.truetype("FreeSansBold.ttf",30)
font_entrynumber = ImageFont.truetype("FreeSansBold.ttf",90)

coord_title = (345, 50)
coord_title2 = (345, 100)

coord_entrytitle = (345,180)
coord_entrynumber = (345,260)

coord_cosplaytitle = (345,360)
coord_cosplayname = (345,410)

coord_judgingtitle = (345,500)
coord_judgingtime = (345,550)



def badge_sticker(entrydetail, num_to_print):
    CurrentJudgingSlot = JudgingSlot.objects.get(pk=entrydetail.judging_time_id)
    CurrentDivision = str(entrydetail.division)
    if CurrentDivision == "Strut Your Stuff" :
        EntryNumber = "SYS" + " " + str(entrydetail.internal_division_number)
    else :
        EntryNumber = CurrentDivision[0] + " " + str(entrydetail.internal_division_number)
        
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle(xy=[0, 0, size[0]-1, size[1]-1 ], fill="white", outline="black", width=1)
    draw.text(coord_title, "AnimeFest/GameFest", fill="black", anchor="mm", font=font_regular)
    draw.text(coord_title2, "Cosplay Runway and Skit Contest", fill="black", anchor="mm", font=font_regular2)
    draw.line([0,150,690,150],fill="black",width=1)
    draw.text(coord_entrytitle, "Entry Number", fill="black", anchor="mm", font=font_judgingtime)
    draw.text(coord_entrynumber, EntryNumber, fill="black", anchor="mm", font=font_entrynumber)
    draw.line([0,315,690,315],fill="black",width=1)
    draw.text(coord_cosplaytitle, "Cosplay Name", fill="black", anchor="mm", font=font_judgingtime)
    draw.text(coord_cosplayname, entrydetail.cosplay_name, fill="black", anchor="mm", font=font_judgingtime)
    draw.line([0,455,690,455],fill="black",width=1)
    draw.text(coord_judgingtitle, "Judging Slot", fill="black", anchor="mm", font=font_judgingtime)
    draw.text(coord_judgingtime, str(CurrentJudgingSlot), fill="black", anchor="mm", font=font_judgingtime)
    
    
    # THESE ARE HARDCODED - HACK
    model = "QL-600"
    backend = "linux_kernel"
    printer = "file:///dev/usb/lp0"
    # END HACK
    from brother_ql.conversion import convert
    from brother_ql.backends.helpers import send
    from brother_ql.raster import BrotherQLRaster
    qlr = BrotherQLRaster(model)
    qlr.exception_on_warning = True
    instructions = convert(qlr=qlr, images=[image, ], label='62', rotate='auto')
    for _ in range(num_to_print):
        send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)
    
size_e = (900, 690)

coord_entrytitle_e = (450, 50)
coord_entrynumber_e = (450, 130)

coord_cosplaytitle_e = (450, 220)
coord_cosplayname_e = (450, 280)

coord_charactertitle = (450, 370)
coord_charactername = (450, 430)
	
coord_seriestitle = (450, 520)
coord_seriesname = (450, 580)
    
def emcee_sticker(entrydetail, num_to_print):

    CurrentDivision = str(entrydetail.division)
    if CurrentDivision == "Strut Your Stuff" :
        EntryNumber = "SYS" + " " + str(entrydetail.internal_division_number)
    else :
        EntryNumber = CurrentDivision[0] + " " + str(entrydetail.internal_division_number)
    
    image = Image.new("RGB", size_e, "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle(xy=[0, 0, size_e[0]-1, size_e[1]-1 ], fill="white", outline="black", width=1)
    draw.text(coord_entrytitle_e, "Entry Number", fill="black", anchor="mm", font=font_judgingtime)
    draw.text(coord_entrynumber_e, EntryNumber, fill="black", anchor="mm", font=font_entrynumber)
    draw.line([0,180,900,180],fill="black",width=1)
	
    draw.text(coord_cosplaytitle_e, "Cosplay Name", fill="black", anchor="mm", font=font_judgingtime)
    draw.text(coord_cosplayname_e, entrydetail.cosplay_name, fill="black", anchor="mm", font=font_regular3)
    draw.line([0,330,900,330],fill="black",width=1)
	
    draw.text(coord_charactertitle, "Character", fill="black", anchor="mm", font=font_judgingtime)
    draw.text(coord_charactername, entrydetail.character, fill="black", anchor="mm", font=font_regular3)
    draw.line([0,480,900,480],fill="black",width=1)
	
    draw.text(coord_seriestitle, "Series", fill="black", anchor="mm", font=font_judgingtime)
    draw.text(coord_seriesname, entrydetail.series, fill="black", anchor="mm", font=font_regular3)

    # THESE ARE HARDCODED - HACK
    model = "QL-600"
    backend = "linux_kernel"
    printer = "file:///dev/usb/lp0"
    # END HACK
    from brother_ql.conversion import convert
    from brother_ql.backends.helpers import send
    from brother_ql.raster import BrotherQLRaster
    qlr = BrotherQLRaster(model)
    qlr.exception_on_warning = True
    instructions = convert(qlr=qlr, images=[image, ], label='62',rotate=0)
    for _ in range(num_to_print):
        send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)
    
