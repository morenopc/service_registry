from django.conf.urls import include, url
from rest_framework import routers
from services.v1.endpoints import registry


router = routers.DefaultRouter()
router.register(r'registries', registry.ServiceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^search/',
        registry.ServiceSearchGenericViewSet.as_view({'get': 'retrieve'}),
        name='search'),
    url(r'^update/(?P<pk>[0-9]+)/$',
        registry.ServiceUpdateAPIView.as_view(),
        name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        registry.ServiceDestroyAPIView.as_view(),
        name='remove'),
]
