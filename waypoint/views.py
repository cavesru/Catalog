from django.shortcuts import render, get_object_or_404

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy

import os
import gpxpy

from object.models import Object
from waypoint.models import Waypoint
from waypoint.forms import WaypointForm

@permission_required('waypoint.add_waypoint')
def waypoint_new(request, pk):
    o = get_object_or_404(Object, pk=pk)
    if request.method == "POST":
        w = WaypointForm(request.POST)
        if w.is_valid():
            w = w.save(commit=False)
            w.owner = request.user
            w.published_date = timezone.now()
            w.object = o
            w.save()
            return render(request, 'object/view.html', {'object': o})
    else:
        w = WaypointForm()
    return render(request, 'waypoint/edit.html', {'waypoint': w})

def waypoint_edit(request, pk, wpk):
    o = get_object_or_404(Object, pk=pk)
    w = get_object_or_404(Waypoint, pk=wpk)
    if not (request.user.has_perm('waypoint.changeown_waypoint') and w.owner == request.user) and not request.user.has_perm('waypoint.change_waypoint'):
        return redirect(reverse_lazy('login'))
    if request.method == "POST":
        w = WaypointForm(request.POST, instance=w)
        if w.is_valid():
            w = w.save(commit=False)
            w.owner = request.user
            w.published_date = timezone.now()
            w.save()
            return render(request, 'object/view.html', {'object': o})
    else:
        w = WaypointForm(instance=w)
    return render(request, 'waypoint/edit.html', {'waypoint': w})
   
def waypoint_delete (request, pk, wpk):
    o = get_object_or_404(Object, pk=pk)
    w = get_object_or_404(Waypoint, pk=wpk)
    if not (request.user.has_perm('waypoint.deleteown_waypoint') and w.owner == request.user) and not request.user.has_perm('waypoint.delete_waypoint'):
        return redirect(reverse_lazy('login'))
    w.delete()
    return render(request, 'object/view.html', {'object': o})

@permission_required('waypoint.add_waypoint')  
def waypoint_load (request, pk):
    o = get_object_or_404(Object, pk=pk)   
    if request.method == 'POST':
        filename = '/Users/andrey/Documents/workspace/Catalog/data/' + str(request.FILES['file'])
        # загружаем файл
        with open(filename, 'wb+') as file:
            for chunk in request.FILES['file'].chunks():
                file.write(chunk)
        # загружаем точки из файла
        file=open(filename)
        gpx = gpxpy.parse(file)
        if gpx.waypoints:        
            for waypoint in gpx.waypoints:            
                if waypoint.name:
                    w=Waypoint()
                    w.name=waypoint.name
                    w.lat=waypoint.latitude
                    w.lon=waypoint.longitude
                    w.owner = request.user
                    w.published_date = timezone.now()
                    w.object=o
                    w.save()
                else:
                    print("Name: unknown")
        file.close()
        os.remove(filename)
    return redirect('object.views.object_view', pk=o.pk)


    
    