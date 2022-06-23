from pyexpat import model
from django.forms import ModelForm
from .models import Prompt

class PromptForm(ModelForm):
    class Meta:
        model = Prompt
        fields = '__all__'