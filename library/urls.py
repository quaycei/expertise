from django.conf.urls import url
from library import views


urlpatterns = [
    url(r'^list', views.library_list, name='library_list'),
    url(r'^create', views.library_create, name='library_create'),
    url(r'^(?P<library_slug>[\w-]+)/update', views.library_update, name='library_update'),
    url(r'^(?P<library_slug>[\w-]+)$', views.library_page, name='library_page'),

    url(r'^(?P<library_slug>[\w-]+)/project/create$', views.project_create, name='project_create'),

    url(r'^(?P<library_slug>[\w-]+)/(?P<project_slug>[\w-]+)$', views.project_page, name='project_page'),

]
