from guardian.shortcuts import assign_perm

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions_app.services import APIPermissionClassFactory
from babies_app.models import Baby
from babies_app.serializers import BabySerializer
from events.models import Event
from events.serializers import EventSerializer

def evaluate(user, obj, request):
    return user.username == obj.parent.first_name

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'babies.view_baby',
                    'destroy': False,
                    'update': True,
                    'partial_update': 'babies.change_baby',
                    'events': evaluate
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        events_by_baby=[]
        for event in Event.objects.filter(baby=baby):
            events_by_baby.append(EventSerializer(event).data)
        return Response(events_by_baby)

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.view_baby', user, baby)
        assign_perm('babies.change_baby', user, baby)
        return Response(serializer.data)

