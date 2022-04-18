# manage_robots/urls.py
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import homePageView


router = routers.DefaultRouter()
router.register(r"position", views.RobotPositionViewSet)
# router.register(r'robots', views.RobotViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("home", homePageView, name="home"),
]
