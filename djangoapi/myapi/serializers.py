from django.db.models.fields import Field
from rest_framework.serializers import ModelSerializer
from .models import input

class inputSerializer(ModelSerializer):
    class Meta:
        model = input
        fields = '__all__'