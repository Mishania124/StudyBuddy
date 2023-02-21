from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerialazer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'