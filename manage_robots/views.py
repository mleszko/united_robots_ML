from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from manage_robots.models import Position, Robot
from manage_robots.serializers import RobotPositionSerializer, RobotSerializer


def homePageView(request):
    return HttpResponse("Main page")


class RobotViewSet(viewsets.ModelViewSet):
    model = Robot
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    permission_classes = [permissions.IsAuthenticated]
    fields = 'name'


class RobotPositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint to check current robot position
    """

    # TODO: filter Positions by robot and display lat one
    model = Position
    queryset = Position.objects.all()  # filter(robot=robot)
    serializer_class = RobotPositionSerializer
    permission_classes = [permissions.IsAuthenticated]
    fields = ('x', 'y', 'datetime', 'robot')

    def list(self, request):
        queryset = Position.objects.all()
        serializer = RobotPositionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Position.objects.all()
        position = get_object_or_404(queryset, pk=pk)
        serializer = RobotPositionSerializer(position)
        return Response(serializer.data)

    def detail(self, request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)