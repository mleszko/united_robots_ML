from django.contrib.auth.models import User, Group
from rest_framework import serializers

from manage_robots.models import Position


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RobotPositionSerializer(serializers.Serializer):
    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance

    class Meta:
        model = Position
        fields = ['x', 'y', 'datetime']
