from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'crud', UserViewSet)


# other URL patterns

urlpatterns = [
    
    path('', include(router.urls)),
]
