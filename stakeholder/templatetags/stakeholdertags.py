from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from stakeholder.models import Cluster, Entity, Stakeholder, Assumption, Stakeholder_Map
from stakeholder.forms import ClusterForm, EntityForm, StakeholderForm, AssumptionForm, Stakeholder_MapForm




register = template.Library()


@register.inclusion_tag('stakeholder/templatetags/list.html')
def stakeholder_list(stakeholder_map_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    stakeholders = Stakeholder.objects.all()
    
    return {'stakeholders':stakeholders,
            'stakeholder_map':stakeholder_map}



@register.inclusion_tag('stakeholder/templatetags/create.html')
def stakeholder_create(stakeholder_map_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    stakeholderform = StakeholderForm()

    if stakeholderform.is_valid():
        stakeholder = stakeholderform.save(commit=False)
        stakeholder.stakeholder_map = stakeholder_map
        stakeholder.save()
        stakeholderform.save_m2m()
        return redirect('stakeholder_map_read')
    
    return {'stakeholder_map':stakeholder_map,
            'stakeholderform':stakeholderform,
           }

@register.inclusion_tag('stakeholder/templatetags/list.html')
def stakeholder_list(stakeholder_map_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    stakeholder = Stakeholder.objects.get(slug=stakeholder_slug)
    
    return {'stakeholder':stakeholder,
            'stakeholder_map':stakeholder_map,
           }


@register.inclusion_tag('stakeholder/templatetags/create.html')
def stakeholder_update(stakeholder_map_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    stakeholderform = StakeholderForm(instance=stakeholder)

    if stakeholderform.is_valid():
        stakeholderform = StakeholderForm(instance=stakeholder)
        stakeholder.save()
        stakeholderform.save_m2m()
        return redirect('stakeholder_map_read')
    
    return {'stakeholderform':stakeholderform,
            'stakeholder_map':stakeholder_map,
           }

