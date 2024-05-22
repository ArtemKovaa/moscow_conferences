from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status, viewsets

from moscow_conferences_api.serializers import ConferenceSerializerDetailed, ConferenceSerializerBrief
from db_module.conference_dao import ConferenceDao
from moscow_conferences_api.conference_exception import ConferenceException
from rest_framework.views import exception_handler
from moscow_conferences_api.models import Conference


class ConferencesViewSet(viewsets.ModelViewSet):

    conference_dao = ConferenceDao()

    @csrf_exempt
    def list(self, _):
        conferences = self.conference_dao.get_all()
        return Response(conferences)

    @csrf_exempt
    def create(self, request):
        conference_data = JSONParser().parse(request)
        conference_serializer = ConferenceSerializerDetailed(data=conference_data)
        if conference_serializer.is_valid():
            self.conference_dao.save(conference_serializer.data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(conference_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def retrieve(self, _, pk=None):
        result = self.conference_dao.get_by_id(pk)
        validate_existence(result, pk)
        conference = Conference(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])
        conference_serializer = ConferenceSerializerDetailed(conference)
        return Response(conference_serializer.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def partial_update(self, request, pk=None):
        conference_data = JSONParser().parse(request)
        result = self.conference_dao.get_by_id(pk)
        validate_existence(result, pk)
        conference_serializer = ConferenceSerializerDetailed(data=conference_data)
        if conference_serializer.is_valid():
            self.conference_dao.update_record(pk, conference_serializer.data)
            return Response(status=status.HTTP_200_OK)
        return Response(conference_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def destroy(self, _, pk=None):
        result = self.conference_dao.get_by_id(pk)
        validate_existence(result, pk)
        self.conference_dao.delete_by_id(pk)
        return Response(status=status.HTTP_200_OK)


def validate_existence(result, conference_id):
    if len(result) == 0:
        raise ConferenceException(detail=f'Conference with id={conference_id} was not found', status_code=404)


def handle_exception(exc, context):
    if isinstance(exc, ConferenceException):
        response_data = {'detail': exc.detail}
        return Response(response_data, status=exc.status_code)
    return exception_handler(exc, context)
