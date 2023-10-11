from rest_framework.serializers import ModelSerializer
from .models import Visitor, Visit, Destination

class VisitorSerializer(ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'

class VisitSerializer(ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
