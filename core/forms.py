from django.forms import ModelForm, TextInput
from .models import city

class cityform(ModelForm):
    class Meta:
        model= city
        fields=['name']
        #widgets= {'name': TextInput(attrs={'çlass':'input', 'placeholder':'City Name'}),}  # This is used to create input form
        widgets = {'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})} 