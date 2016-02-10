"""Catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

from waypoint import views as waypoint_views
from object import views as object_views
from album import views as album_views
from photo import views as photo_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', object_views.object_list, name='index'),
    url(r'^object/$', object_views.object_list, name='object_list'),
    url(r'^object/new$', object_views.object_new, name='object_new'),
    url(r'^object/(?P<pk>[0-9]+)/$', object_views.object_view, name='object_view'),
    url(r'^object/(?P<pk>[0-9]+)/edit/$', object_views.object_edit, name='object_edit'),
    url(r'^object/(?P<pk>[0-9]+)/waypointnew/$', waypoint_views.waypoint_new, name='waypoint_new'),
    url(r'^object/(?P<pk>[0-9]+)/waypointload/$', waypoint_views.waypoint_load, name='waypoint_load'),
    url(r'^object/(?P<pk>[0-9]+)/waypoint/(?P<wpk>[0-9]+)/edit/$', waypoint_views.waypoint_edit, name='waypoint_edit'),
    url(r'^object/(?P<pk>[0-9]+)/waypoint/(?P<wpk>[0-9]+)/delete/$', waypoint_views.waypoint_delete, name='waypoint_delete'),
    url(r'^object/(?P<pk>[0-9]+)/albumnew/$', album_views.album_new, name='album_new'),
    url(r'^object/(?P<pk>[0-9]+)/album/(?P<apk>[0-9]+)/edit/$', album_views.album_edit, name='album_edit'),
    url(r'^object/(?P<pk>[0-9]+)/album/(?P<apk>[0-9]+)/delete/$', album_views.album_delete, name='album_delete'),
    url(r'^object/(?P<pk>[0-9]+)/album/(?P<apk>[0-9]+)/$', album_views.album_view, name='album_view'),
    url(r'^object/(?P<pk>[0-9]+)/album/(?P<apk>[0-9]+)/photoload/$',photo_views.photo_load, name='photo_load'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)