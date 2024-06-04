from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from .views import RecursoViewSet, ReservaViewSet, UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'recursos', RecursoViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]