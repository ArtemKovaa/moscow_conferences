from rest_framework import serializers
from moscow_conferences_api.models import Location, Conference


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ('id', 'name', 'description', 'start_date', 'location')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address')