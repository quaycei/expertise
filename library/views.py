from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from library.models import Library, Project
from library.forms import LibraryForm, ProjectForm



def library_list(request):
    librarys = Library.objects.all()

    return render(request, 'library/list.html', {'librarys':librarys})


def library_page(request, library_slug):
    library = Library.objects.get(slug=library_slug)
    projects = Project.objects.filter(library=library)

    return render(request, 'library/page.html',{
        'library':library,
        'projects':projects,
         })
       

def library_create(request):
    libraryform = LibraryForm()
    
    if request.method == 'POST':
        libraryform = LibraryForm(request.POST)
        if libraryform.is_valid():
            library = libraryform.save(commit=False)
            library.creator = request.user
            library.save()
            libraryform.save_m2m()
            return redirect(library_read, {'library':library})
    
    return render(request, 'library/templatetags/create.html',{
            'libraryform':libraryform
        })


def library_update(request, library_slug):
    library = Library.objects.get(slug=library_slug)
    libraryform = LibraryForm(instance=library)
    
    if request.method == 'POST':
        libraryform = LibraryForm(request.POST, instance=library)
        if libraryform.is_valid():
            library = libraryform.save()
            return redirect(library_read, {'library':library})
    
    return render(request, 'library/templatetags/create.html',{
            'libraryform':libraryform, 'library':library
        })




def project_create(request, library_slug):
    projectform = ProjectForm()
    library = Library.objects.get(slug=library_slug)
    
    if request.method == 'POST':
        projectform = ProjectForm(request.POST)
        if projectform.is_valid():
            project = projectform.save(commit=False)
            project.creator = request.user
            project.save()
            projectform.save_m2m()
            return redirect(project_page, {'library':library, 'project':project})
    
    return render(request, 'project/templatetags/create.html',{
            'library':library,
            'projectform':projectform,
        })



def project_page(request, library_slug, project_slug):
    library = Library.objects.get(slug=library_slug)
    project = Project.objects.get(slug=project_slug)

    return render(request, 'library/page.html',{
            'library':library,
            'project':project,
        })





