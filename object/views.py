from django.shortcuts import render, get_object_or_404

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import permission_required

from object.models import Object
from object.forms import ObjectForm

def object_list (request):
    object_list = Object.objects.all()
    return render(request,'object/list.html', {'object_list':object_list})

def object_view(request, pk):
    o = get_object_or_404(Object, pk=pk)
    return render(request, 'object/view.html', {'object': o})

def object_new(request):
    if request.method == "POST":
        o = ObjectForm(request.POST)
        if o.is_valid():
            o = o.save(commit=False)
            o.owner = request.user
            o.published_date = timezone.now()
            o.save()
            return redirect('object.views.object_list')
    else:
        o = ObjectForm()
    return render(request, 'object/edit.html', {'object': o})
    
def object_edit(request, pk):
    o = get_object_or_404(Object, pk=pk)
    if request.method == "POST":
        o = ObjectForm(request.POST, instance=o)
        if o.is_valid():
            o = o.save(commit=False)
            o.owner = request.user
            o.published_date = timezone.now()
            o.save()
            return redirect('object.views.object_view', pk=o.pk)
    else:
        o = ObjectForm(instance=o)
    return render(request, 'object/edit.html', {'object': o})