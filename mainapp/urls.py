from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import *
import mainapp.views as views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^two_gis_view/$',views.two_gis_view)
]