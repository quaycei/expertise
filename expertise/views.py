from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from stakeholder.models import Stakeholder_Map
from stakeholder.forms import Stakeholder_MapForm



def splash(request):
    return redirect('mindel_home')


