from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status, viewsets

from moscow_conferences_api.models import Location, Conference
from moscow_conferences_api.serializers import LocationSerializer, ConferenceSerializer


class ConferencesViewSet(viewsets.ModelViewSet):

    @csrf_exempt
    def list(self, request):
        queryset = Conference.objects.all()
        conference_serializer = ConferenceSerializer(queryset, many=True)
        return Response(conference_serializer.data)

    @csrf_exempt
    def create(self, request):
        conference_data = JSONParser().parse(request)
        conference_serializer = ConferenceSerializer(data=conference_data)
        if conference_serializer.is_valid():
            conference_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(conference_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def retrieve(self, request, pk=None):
        queryset = Conference.objects.all()
        conference = get_object_or_404(queryset, pk=pk)
        conference_serializer = ConferenceSerializer(conference)
        return Response(conference_serializer.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def partial_update(self, request, pk=None):
        conference_data = JSONParser().parse(request)
        queryset = Conference.objects.all()
        conference = get_object_or_404(queryset, pk=pk)
        conference_serializer = ConferenceSerializer(conference, data=conference_data)
        if conference_serializer.is_valid():
            conference_serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(conference_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def destroy(self, conference_id):
        conference = Conference.objects.get(id=conference_id)
        conference.delete()
        return Response(status=status.HTTP_200_OK)
