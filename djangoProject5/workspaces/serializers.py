from rest_framework import serializers
from workspaces.models import Workspace


class WorkspaceSerializer(
    serializers.ModelSerializer):
    admins = serializers.ListField(
        child=serializers.IntengerField
    )
    members = serializers.ListField(
        child=serializers.IntegerField
    )

    class Meta:
        model = Workspace
        fields = '__all__'
