from django.shortcuts import render
# from django.http import HttpResponse
from django.utils.translation import gettext as _
import datetime

def view_home(request, *args, **kwargs):
    print(_("Logged as:"), request.user, "!")
    return render(request, "home.html", {'date': datetime.date})

