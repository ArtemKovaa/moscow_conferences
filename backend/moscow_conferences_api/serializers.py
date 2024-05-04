from rest_framework import serializers
from moscow_conferences_api.models import Conference


class ConferenceSerializerDetailed(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'


class ConferenceSerializerBrief(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ('id', 'name')
