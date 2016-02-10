from django import forms

from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', )
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Имя" 