from django.shortcuts import render, get_object_or_404

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

from object.models import Object
from album.models import Album
from album.forms import AlbumForm

@permission_required('album.add_album')
def album_new(request, pk):
    o = get_object_or_404(Object, pk=pk)
    if request.method == "POST":
        a = AlbumForm(request.POST)
        if a.is_valid():
            a = a.save(commit=False)
            a.owner = request.user
            a.published_date = timezone.now()
            a.object = o
            a.save()
            return redirect('object.views.object_view', pk=o.pk)
    else:
        a = AlbumForm()
    return render(request, 'album/edit.html', {'album': a})

def album_edit(request, pk, apk):
    o = get_object_or_404(Object, pk=pk)
    a = get_object_or_404(Album, pk=apk)
    if not (request.user.has_perm('album.changeown_album') and a.owner == request.user) and not request.user.has_perm('album.change_album'):
        return redirect(reverse_lazy('login'))
    if request.method == "POST":
        a = AlbumForm(request.POST, instance=a)
        if a.is_valid():
            a = a.save(commit=False)
            a.owner = request.user
            a.published_date = timezone.now()
            a.save()
            return redirect('object.views.object_view', pk=o.pk)
    else:
        a = AlbumForm(instance=a)
    return render(request, 'album/edit.html', {'album': a})

@permission_required('album.deleteown_album')    
def album_delete (request, pk, apk):
    o = get_object_or_404(Object, pk=pk)
    a = get_object_or_404(Album, pk=apk)
    if not (request.user.has_perm('album.deleteown_album') and a.owner == request.user) and not request.user.has_perm('album.delete_album'):
        return redirect(reverse_lazy('login'))
    a.delete()
    return render(request, 'object/view.html', {'object': o})
    
def album_view(request, pk , apk):
    o = get_object_or_404(Object, pk=pk)
    a = get_object_or_404(Album, pk=apk)
    return render(request, 'album/view.html', {'album': a})