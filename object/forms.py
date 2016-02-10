from django import forms

from .models import Object

class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ('name', 'length',)
    def __init__(self, *args, **kwargs):
        super(ObjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Имя" 
        self.fields['name'].label = "Протяженность"        

        
        
