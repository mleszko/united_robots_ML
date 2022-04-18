from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from manage_robots.models import Position
from manage_robots.serializers import RobotPositionSerializer

def homePageView(request):
    return HttpResponse("Main page")

class RobotPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint to check current robot position
    """
    #TODO: filter Positions by robot and display lat one
    queryset = Position.objects.all() #filter(robot=robot)
    serializer_class = RobotPositionSerializer
    permission_classes = [permissions.IsAuthenticated]
