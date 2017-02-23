from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from library.models import Library, Project
from hopefear.models import Hopefear_Map, Thought
from hopefear.forms import Hopefear_MapForm, ThoughtForm


def hopefear_map_list(request):
    hopefear_maps = Hopefear_Map.objects.all()

    return render(request, 'hopefear/list.html', {'hopefear_maps':hopefear_maps})


def hopefear_map_page(request, hopefear_map_slug):
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)

    return render(request, 'hopefear/page.html',{'hopefear_map':hopefear_map}) 


def hopefear_map(request, hopefear_map_slug):
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)
    thoughts = Thought.objects.all()

    return render(request, 'hopefear/map/page.html',{'hopefear_map':hopefear_map, 'thoughts':thoughts}) 
       
def hopefear_map_remote(request, hopefear_map_slug):
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)
    
    return render(request, 'hopefear/remote.html',{
            'hopefear_map':hopefear_map,
        })



def hopefear_map_create(request):
    hopefear_mapform = Hopefear_MapForm()
    
    if request.method == 'POST':
        hopefear_mapform = Hopefear_MapForm(request.POST)
        if hopefear_mapform.is_valid():
            hopefear_map = hopefear_mapform.save(commit=False)
            hopefear_map.creator = request.user
            hopefear_map.save()
            hopefear_mapform.save_m2m()
            return redirect(hopefear_map_page, {'hopefear_map':hopefear_map})
    
    return render(request, 'hopefear/templatetags/create.html',{
            'hopefear_mapform':hopefear_mapform
        })


def hopefear_map_update(request, hopefear_map_slug):
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)
    hopefear_mapform = Hopefear_MapForm(instance=hopefear_map)
    
    if request.method == 'POST':
        hopefear_mapform = Hopefear_MapForm(request.POST, instance=hopefear_map)
        if hopefear_mapform.is_valid():
            hopefear_map = hopefear_mapform.save()
            return redirect(hopefear_map_read, {'hopefear_map':hopefear_map})
    
    return render(request, 'hopefear_map/templatetags/create.html',{
            'hopefear_mapform':hopefear_mapform, 'hopefear_map':hopefear_map
        })




def thought_create(request, hopefear_map_slug):
    thoughtform = ThoughtForm()
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)
    
    if request.method == 'POST':
        thoughtform = ThoughtForm(request.POST)
        if thoughtform.is_valid():
            thought = thoughtform.save(commit=False)
            thought.creator = request.user
            thought.save()
            thoughtform.save_m2m()
            return redirect(thought_page, {'hopefear_map':hopefear_map, 'thought':thought})
    
    return render(request, 'thought/templatetags/create.html',{
            'hopefear_map':hopefear_map,
            'thoughtform':thoughtform,
        })



def thought_page(request, hopefear_map_slug, thought_id):
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)
    thought = Thought.objects.get(slug=thought_id)

    return render(request, 'hopefear_map/page.html',{
            'hopefear_map':hopefear_map,
            'thought':thought,
        })





