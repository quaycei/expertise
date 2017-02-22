from django.conf.urls import url
from stakeholder import views


urlpatterns = [
    url(r'^mindel', views.mindel_home, name='mindel_home'),
    url(r'^stakeholder', views.stakeholder_splash, name='stakeholder_splash'),

    url(r'^(?P<stakeholder_map_slug>[\w-]+)/stakeholder/list', views.stakeholder_list, name='stakeholder_list'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/stakeholder/create', views.stakeholder_create, name='stakeholder_create'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/stakeholder/(?P<stakeholder_slug>[\w-]+)/update$', views.stakeholder_update, name='stakeholder_update'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/stakeholder/(?P<stakeholder_slug>[\w-]+)$', views.stakeholder_read, name='stakeholder_read'),


    url(r'^(?P<stakeholder_map_slug>[\w-]+)/cluster/list', views.cluster_list, name='cluster_list'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/cluster/create', views.cluster_create, name='cluster_create'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/cluster/(?P<cluster_slug>[\w-]+)/update$', views.cluster_update, name='cluster_update'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/cluster/(?P<cluster_slug>[\w-]+)$', views.cluster_read, name='cluster_read'),

    url(r'^(?P<stakeholder_map_slug>[\w-]+)/entity/list', views.entity_list, name='entity_list'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/entity/create', views.entity_create, name='entity_create'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/entity/(?P<entity_slug>[\w-]+)/update$', views.entity_update, name='entity_update'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/entity/(?P<entity_slug>[\w-]+)$', views.entity_read, name='entity_read'),


    url(r'^(?P<stakeholder_map_slug>[\w-]+)/assumption/list', views.assumption_list, name='assumption_list'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/assumption/create', views.assumption_create, name='assumption_create'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/assumption/(?P<assumption_slug>[\w-]+)/update$', views.assumption_update, name='assumption_update'),
    url(r'^(?P<stakeholder_map_slug>[\w-]+)/assumption/(?P<assumption_slug>[\w-]+)$', views.assumption_read, name='assumption_read'),

    url(r'^smap/list', views.stakeholder_map_list, name='stakeholder_map_list'),
    url(r'^smap/create', views.stakeholder_map_create, name='stakeholder_map_create'),
    url(r'^smap/(?P<stakeholder_map_slug>[\w-]+)/update$', views.stakeholder_map_update, name='stakeholder_map_update'),
    url(r'^smap/(?P<stakeholder_map_slug>[\w-]+)$', views.stakeholder_map_read, name='stakeholder_map_read'),
]
