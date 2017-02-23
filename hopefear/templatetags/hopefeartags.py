from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from library.models import Library, Project
from hopefear.forms import Hopefear_MapForm, ThoughtForm
from hopefear.models import Hopefear_Map, Thought





register = template.Library()



@register.inclusion_tag('hopefear_map/templatetags/create.html')
def hopefear_map_create():
    hopefear_mapform = Hopefear_MapForm()

    if hopefear_mapform.is_valid():
        hopefear_map = hopefear_mapform.save(commit=False)
        hopefear_map.save()
        hopefear_mapform.save_m2m()
        return redirect('hopefear_map_page', {'hopefear_map':hopefear_map})
    
    return {
            'hopefear_mapform':hopefear_mapform,
           }


@register.inclusion_tag('hopefear/map/page.html')
def hopefear_map_read(hopefear_map_slug):
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)

    return {
            'hopefear_map':hopefear_map,
           }
       


@register.inclusion_tag('hopefear/templatetags/thought/create.html')
def thought_create(hopefear_map_slug):
    hopefear_map = Hopefear_Map.objects.get(slug=hopefear_map_slug)
    thoughtform = ThoughtForm()

    if thoughtform.is_valid():
        thought = thoughtform.save(commit=False)
        thought.hopefear_map = hopefear_map
        thought.save()
        thoughtform.save_m2m()
 
        return redirect('thought_create', {'hopefear_map':hopefear_map})
    
    return {
            'hopefear_map':hopefear_map,
            'thoughtform':thoughtform,
           }


@register.inclusion_tag('thought/templatetags/read.html')
def thought_read(thought_slug):
    thought = Thought.objects.get(slug=thought_slug)
    hopefear_maps = Hopefear_Map.objects.all()



    return {
            'thought':thought,
            'hopefear_maps':hopefear_maps,
           }

