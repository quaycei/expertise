from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from library.models import Library, Project
from library.forms import LibraryForm, ProjectForm
from hopefear.models import Hopefear_Map




register = template.Library()



@register.inclusion_tag('library/templatetags/create.html')
def library_create():
    libraryform = LibraryForm()

    if libraryform.is_valid():
        library = libraryform.save(commit=False)
        library.save()
        libraryform.save_m2m()
        return redirect('library_page', {'library':library})
    
    return {
            'libraryform':libraryform,
           }


@register.inclusion_tag('library/templatetags/read.html')
def library_read(library_slug):
    library = Library.objects.get(slug=library_slug)

    return {
            'library':library,
           }
       


@register.inclusion_tag('project/templatetags/create.html')
def project_create(library_slug):
    library = Library.objects.get(slug=library_slug)
    projectform = ProjectForm()

    if projectform.is_valid():
        project = projectform.save(commit=False)
        project.save()
        projectform.save_m2m()
        return redirect('project_page', {'project':project})
    
    return {
            'library':library,
            'projectform':projectform,
           }


@register.inclusion_tag('project/templatetags/read.html')
def project_read(project_slug):
    project = Project.objects.get(slug=project_slug)
    hopefear_maps = Hopefear_Map.objects.filter(project=project)



    return {
            'project':project,
            'hopefear_maps':hopefear_maps,
           }

