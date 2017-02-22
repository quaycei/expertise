from django.forms.models import ModelForm
from library.models import Library, Project

class LibraryForm(ModelForm):
	class Meta:
		model = Library
		exclude = ['creator', 'created_at',]


class ProjectForm(ModelForm):
	class Meta:
		model = Project
		exclude = ['creator', 'created_at',]


