from guardian.shortcuts import assign_perm

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer

from permissions_app.services import APIPermissionClassFactory


def evaluate(user, obj, request):
    return user.username == obj.baby.parent.first_name

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': evaluate,
                    'update': evaluate,
                    'partial_update': 'events.change_event',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby=serializer.validated_data["baby"]
        user = self.request.user
        user_name=str(user.username)
        parent_name=baby.get_baby_parent()
        
        if (user_name!=parent_name):
            return Response("Este bebe no pertenece a la familia de " + parent_name)
        else:
            event = serializer.save()
            assign_perm('events.change_event', user, event)
            assign_perm('events.view_event', user, event)
            return Response(serializer.data)