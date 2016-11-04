from rest_framework import serializers
from django.utils.cache import force_text
from encrypted_id import ekey
from .models import EPCompany


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = EPCompany
        fields = ('id', 'company_name')

    def get_id(self, obj):
        return force_text(ekey(obj))
