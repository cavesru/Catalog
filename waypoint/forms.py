from django import forms


from .models import Waypoint

class WaypointForm(forms.ModelForm):
    class Meta:
        model = Waypoint
        fields = ('name','lat', 'lon', )
    def __init__(self, *args, **kwargs):
        super(WaypointForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Имя" 
        self.fields['lat'].label  = "Широта"
        self.fields['lon'].label  = "Долгота"  
