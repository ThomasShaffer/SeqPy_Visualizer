from rest_framework.serializers import ModelSerializer
from .models import Dna


class DnaSerializer(ModelSerializer):
    class Meta:
        model = Dna
        fields = '__all__'

