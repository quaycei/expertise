from django.forms.models import ModelForm
from stakeholder.models import Stakeholder_Map, Cluster, Entity, Stakeholder,Assumption

class ClusterForm(ModelForm):
	class Meta:
		model = Cluster
		exclude = ['creator', 'created_at',]

class EntityForm(ModelForm):
	class Meta:
		model = Entity
		exclude = ['creator', 'created_at',]

class StakeholderForm(ModelForm):
	class Meta:
		model = Stakeholder
		exclude = ['creator', 'created_at',]

class AssumptionForm(ModelForm):
	class Meta:
		model = Assumption
		exclude = ['creator', 'created_at',]

class Stakeholder_MapForm(ModelForm):
	class Meta:
		model = Stakeholder_Map
		exclude = ['creator', 'created_at',]



