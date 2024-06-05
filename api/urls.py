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

#Pequeño script para crear token a los usuarios
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user = user)