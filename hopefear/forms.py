from django.forms.models import ModelForm
from hopefear.models import Hopefear_Map, Thought

class Hopefear_MapForm(ModelForm):
	class Meta:
		model = Hopefear_Map
		exclude = ['creator', 'created_at',]


class ThoughtForm(ModelForm):
	class Meta:
		model = Thought
		exclude = ['creator', 'created_at',]


