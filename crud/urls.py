from django.conf.urls import url
from .views import index
from .views import editar

urlpatterns = [
    url(r'^$', index, name='crudindex'),
    url(r'^editar/(?P<pk>[0-9]+)$', editar, name='crudeditar'), # url(r'^editar$', editar, name='crudeditar'),
]
