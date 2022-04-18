from django.contrib import admin

# Register your models here.
from manage_robots.models import Robot, Position


class RobotAdmin(admin.ModelAdmin):
    fields = ("name", )
    pass


class PositionAdmin(admin.ModelAdmin):
    fields = ("x", "y", "datetime", "robot")
    pass


admin.site.register(Robot, RobotAdmin)
admin.site.register(Position, PositionAdmin)
