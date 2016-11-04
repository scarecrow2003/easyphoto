from rest_framework import serializers
from encrypted_id import ekey
from .models import EPCompany


class CompanySerializer(serializers.ModelSerializer):
    eid = serializers.SerializerMethodField()

    class Meta:
        model = EPCompany
        fields = '__all__'
        #fields = ('eid', 'company_name')

    def get_eid(self, obj):
        return ekey(obj.id)
