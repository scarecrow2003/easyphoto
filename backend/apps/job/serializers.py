from rest_framework import serializers
from .models import EPJob


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPJob
        fields = ('customer_name', 'customer')
