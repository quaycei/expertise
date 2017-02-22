from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from stakeholder.models import Cluster, Entity, Stakeholder, Assumption, Stakeholder_Map
from stakeholder.forms import ClusterForm, EntityForm, StakeholderForm, AssumptionForm, Stakeholder_MapForm



def mindel_home(request):
    return render(request, 'mindel_home.html')
        

def stakeholder_splash(request):
    stakeholder_mapform = Stakeholder_MapForm()
    stakeholders = Stakeholder.objects.all()
    entitys = Entity.objects.all()
    assumptions = Assumption.objects.all()
    clusters = Cluster.objects.all()
    stakeholder_maps = Stakeholder_Map.objects.all()

    return render(request, 'stakeholder_splash.html', {
            'stakeholder_mapform':stakeholder_mapform,
            'stakeholders':stakeholders,
            'entitys':entitys,
            'assumptions':assumptions,
            'clusters':clusters,
            'stakeholder_maps':stakeholder_maps,
        })




def cluster_list(request):
    clusters = Cluster.objects.all()

    return render(request, 'cluster/list.html', {'clusters':clusters})


def cluster_create(request):
    clusterform = ClusterForm()
    
    if request.method == 'POST':
        clusterform = ClusterForm(request.POST)
        if clusterform.is_valid():
            cluster = clusterform.save(commit=False)
            cluster.creator = request.user
            cluster.save()
            clusterform.save_m2m()
            return redirect(stakeholder_map_read, {'stakeholder_map':stakeholder_map})
    
    return render(request, 'cluster/create.html',{
            'clusterform':clusterform
        })


def cluster_update(request, cluster_slug):
    cluster = Cluster.objects.get(slug=cluster_slug)
    clusterform = ClusterForm(instance=cluster)
    
    if request.method == 'POST':
        clusterform = ClusterForm(request.POST, instance=cluster)
        if clusterform.is_valid():
            cluster = clusterform.save()
            return redirect(stakeholder_splash)
    
    return render(request, 'cluster/create.html',{
            'clusterform':clusterform, 'cluster':cluster
        })


def cluster_read(request, cluster_slug):
    cluster = Cluster.objects.get(slug=cluster_slug)
    assumptions = Assumption.objects.all()

    return render(request, 'cluster/read.html', {
            'cluster':cluster,
            'assumptions':assumptions
        })



def entity_list(request):
    entitys = Entity.objects.all()

    return render(request, 'entity/list.html', {'entitys':entitys})


def entity_create(request, stakeholder_map_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    entityform = EntityForm()
    
    if request.method == 'POST':
        entityform = EntityForm(request.POST)
        if entityform.is_valid():
            entity = entityform.save(commit=False)
            entity.creator = request.user
            entity.stakeholder_map = stakeholder_map
            entity.save()
            entityform.save_m2m()
            return redirect('stakeholder_map_list')
    
    return render(request, 'entity/create.html',{'stakeholder_map':stakeholder_map,
            'entityform':entityform,
            
        })


def entity_update(request, stakeholder_map_slug, entity_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    entity = Entity.objects.get(slug=entity_slug)
    entityform = EntityForm(instance=entity)
    
    if request.method == 'POST':
        entityform = EntityForm(request.POST, instance=entity)
        if entityform.is_valid():
            entity = entityform.save()
            return redirect(stakeholder_splash)
    
    return render(request, 'entity/create.html',{
            'entityform':entityform, 'entity':entity, 'stakeholder_map':stakeholder_map
        })


def entity_read(request, stakeholder_map_slug, entity_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    entity = Entity.objects.get(slug=entity_slug)

    return render(request, 'entity/read.html', {
            'stakeholder_map':stakeholder_map, 'entity':entity
        })






def stakeholder_list(request):
    stakeholders = Stakeholder.objects.all()

    return render(request, 'stakeholder/list.html', {'stakeholders':stakeholders})


def stakeholder_create(request):
    stakeholderform = StakeholderForm()
    
    if request.method == 'POST':
        stakeholderform = StakeholderForm(request.POST)
        if stakeholderform.is_valid():
            stakeholder = stakeholderform.save(commit=False)
            stakeholder.creator = request.user
            stakeholder.save()
            stakeholderform.save_m2m()
            return redirect(stakeholder_map_read, {'stakeholder_map':stakeholder_map})
    
    return render(request, 'stakeholder/create.html',{
            'stakeholderform':stakeholderform,
        })


def stakeholder_update(request, stakeholder_slug):
    stakeholder = Stakeholder.objects.get(slug=stakeholder_slug)
    stakeholderform = StakeholderForm(instance=stakeholder)
    
    if request.method == 'POST':
        stakeholderform = StakeholderForm(request.POST, instance=stakeholder)
        if stakeholderform.is_valid():
            stakeholder = stakeholderform.save()
            return redirect(stakeholder_splash)
    
    return render(request, 'stakeholder/create.html',{
            'stakeholderform':stakeholderform, 'stakeholder':stakeholder
        })


def stakeholder_read(request, stakeholder_slug):
    stakeholder = Stakeholder.objects.get(slug=stakeholder_slug)

    return render(request, 'stakeholder/read.html', {
            'stakeholder':stakeholder,
        })


def assumption_list(request):
    assumptions = Assumption.objects.all()

    return render(request, 'assumption/list.html', {'assumptions':assumptions})


def assumption_create(request):
    assumptionform = AssumptionForm()
    
    if request.method == 'POST':
        assumptionform = AssumptionForm(request.POST)
        if assumptionform.is_valid():
            assumption = assumptionform.save(commit=False)
            assumption.creator = request.user
            assumption.save()
            assumptionform.save_m2m()
            return redirect(stakeholder_map_read, {'stakeholder_map':stakeholder_map})
    
    return render(request, 'assumption/create.html',{
            'assumptionform':assumptionform
        })


def assumption_update(request, assumption_slug):
    assumption = Assumption.objects.get(slug=assumption_slug)
    assumptionform = AssumptionForm(instance=assumption)
    
    if request.method == 'POST':
        assumptionform = AssumptionForm(request.POST, instance=assumption)
        if assumptionform.is_valid():
            assumption = assumptionform.save()
            return redirect(stakeholder_map_read, {'stakeholder_map':stakeholder_map})
    
    return render(request, 'assumption/create.html',{
            'assumptionform':assumptionform, 'assumption':assumption
        })


def assumption_read(request, assumption_slug):
    assumption = Assumption.objects.get(slug=assumption_slug)
    stakeholders = Stakeholder.objects.filter(assumption=assumption)


    return render(request, 'assumption/read.html', {
            'assumption':assumption,
            'stakeholders':stakeholders
        })

def stakeholder_map_list(request):
    stakeholder_maps = Stakeholder_Map.objects.all()

    return render(request, 'stakeholder_map/list.html', {'stakeholder_maps':stakeholder_maps})


def stakeholder_map_create(request):
    stakeholder_mapform = Stakeholder_MapForm()
    
    if request.method == 'POST':
        stakeholder_mapform = Stakeholder_MapForm(request.POST)
        if stakeholder_mapform.is_valid():
            stakeholder_map = stakeholder_mapform.save(commit=False)
            stakeholder_map.creator = request.user
            stakeholder_map.save()
            stakeholder_mapform.save_m2m()
            return redirect(stakeholder_map_read, {'stakeholder_map':stakeholder_map})
    
    return render(request, 'stakeholder_map/create.html',{
            'stakeholder_mapform':stakeholder_mapform
        })


def stakeholder_map_update(request, stakeholder_map_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    stakeholder_mapform = Stakeholder_MapForm(instance=stakeholder_map)
    
    if request.method == 'POST':
        stakeholder_mapform = Stakeholder_MapForm(request.POST, instance=stakeholder_map)
        if stakeholder_mapform.is_valid():
            stakeholder_map = stakeholder_mapform.save()
            return redirect(stakeholder_splash)
    
    return render(request, 'stakeholder_map/create.html',{
            'stakeholder_mapform':stakeholder_mapform, 'stakeholder_map':stakeholder_map
        })


def stakeholder_map_read(request, stakeholder_map_slug):
    stakeholder_map = Stakeholder_Map.objects.get(slug=stakeholder_map_slug)
    stakeholders = Stakeholder.objects.all()
    entitys = Entity.objects.filter(stakeholder_map=stakeholder_map)
    assumptions = Assumption.objects.filter(stakeholder_map=stakeholder_map)
    clusters = Cluster.objects.filter(stakeholder_map=stakeholder_map)
    stakeholderform = StakeholderForm()
    assumptionform = AssumptionForm()
    clusterform = ClusterForm()
    entityform = EntityForm()
    stakeholder_mapform = Stakeholder_MapForm()
    

    return render(request, 'stakeholder_map/read.html', {
            'stakeholder_map':stakeholder_map,
            'stakeholders':stakeholders,
            'entitys':entitys,
            'assumptions':assumptions,
            'clusters':clusters,
            'stakeholderform':stakeholderform,
            'assumptionform':assumptionform,
            'clusterform':clusterform,
            'entityform':entityform,
            'stakeholder_mapform':stakeholder_mapform,

        })


