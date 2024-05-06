from django import forms
from .models import Machine, MachineImage
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'manufacturer', 'year_manufactured', 'serial_number', 'machine_type']

class MachineImageForm(forms.ModelForm):
    class Meta:
        model = MachineImage
        fields = ['image']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']