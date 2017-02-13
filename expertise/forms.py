from django.forms.models import ModelForm
from stakeholder.models import Stakeholder

class StakeholderForm(ModelForm):
	class Meta:
		model = Feedback
		exclude = ['creator', 'created_at',]

