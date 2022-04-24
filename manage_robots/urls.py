# manage_robots/urls.py
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import homePageView


router = routers.DefaultRouter()
router.register(r"positions", views.RobotPositionViewSet)
router.register(r'robots', views.RobotViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # path('<int:position_id>/', views.RobotPositionViewSet.detail, name='detail'),
    path("home", homePageView, name="home"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
