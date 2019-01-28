from django.forms import ModelForm
from .models import Candidate, Position

class CandidateModelForm(ModelForm):
    class Meta:
        model=Candidate
        exclude=['id']

class AskForm(ModelForm):
    class Meta:
        model = Candidate
        exclude =['id']

class AskForm2(ModelForm):
    class Meta:
        model = Position
        exclude =['id']
