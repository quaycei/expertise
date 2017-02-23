from django.conf.urls import url
from hopefear import views


urlpatterns = [
    url(r'^list', views.hopefear_map_list, name='hopefear_map_list'),
    url(r'^create', views.hopefear_map_create, name='hopefear_map_create'),
    url(r'^(?P<hopefear_map_slug>[\w-]+)/update', views.hopefear_map_update, name='hopefear_map_update'),
    url(r'^(?P<hopefear_map_slug>[\w-]+)$', views.hopefear_map_page, name='hopefear_map_page'),
    url(r'^map/(?P<hopefear_map_slug>[\w-]+)$', views.hopefear_map, name='hopefear_map'),
    url(r'^remote/(?P<hopefear_map_slug>[\w-]+)$', views.hopefear_map_remote, name='hopefear_map_remote'),

    url(r'^(?P<hopefear_map_slug>[\w-]+)/thought/create$', views.thought_create, name='thought_create'),
    url(r'^(?P<hopefear_map_slug>[\w-]+)/(?P<thought_id>[\w-]+)$', views.thought_page, name='thought_page'),
]
