from django.contrib.auth.forms import UserCreationForm
from .models import DGIUser,Candidat,Agent
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = DGIUser
        fields = ("email","first_name","last_name")

class CandidatForm(ModelForm):
    class Meta:
        model = Candidat
        exclude = ("user","compte","formation_asked","is_confirmed")

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ("matricule","is_laborantin","profession")

