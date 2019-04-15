from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('games', views.GameViewSet)

app_name = 'games'

urlpatterns = [
    path('', include(router.urls))
]
