from django.contrib.auth.models import User, Group
from rest_framework import serializers

from manage_robots.models import Position, Robot


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class RobotSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

    name = serializers.CharField()

    def create(self, validated_data):
        return Robot.objects.create(**validated_data)


class RobotPositionSerializer(serializers.Serializer):
    robot = serializers.PrimaryKeyRelatedField(queryset=Robot.objects.all())
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    datetime = serializers.DateTimeField()

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.x = validated_data.get("x", instance.x)
        instance.y = validated_data.get("y", instance.y)
        instance.robot = validated_data.get("robot", instance.robot)
        instance.datetime = validated_data.get("datetime", instance.datetime)
        instance.save()
        return instance

    class Meta:
        model = Position
        fields = ["x", "y", "datetime"]
