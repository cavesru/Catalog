from django.shortcuts import render, get_object_or_404

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone

from object.models import Object
from photo.models import Photo
from album.models import Album

def photo_load (request, pk, apk):
    o = get_object_or_404(Object, pk=pk) 
    a = get_object_or_404(Album, pk=apk)   
    if request.method == 'POST': 
        for file in request.FILES.getlist('file'):
            p = Photo()
            p.owner = request.user
            p.published_date = timezone.now()  
            p.album = a
            p.photo.save(str(file),file,save=True)
            p.thumb_make()          
            p.save()           
    return redirect('object.views.object_view', pk=o.pk) 