from django.urls import path, include
from characters import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'characters', views.CharacterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

