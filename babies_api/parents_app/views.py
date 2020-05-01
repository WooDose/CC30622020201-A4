from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from babies_app.serializers import BabySerializer
from babies_app.models import Baby
from parents_app.models import Parent
from parents_app.serializers import ParentSerializer

from permissions_app.services import APIPermissionClassFactory



class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    @action(detail=True, methods=['get'])
    def babies(self, request, pk=None):
        parent = self.get_object()
        children_for_user = []
        for kid in Baby.objects.filter(parent=parent):
            children_for_user.append(BabySerializer(kid).data)
        return Response(children_for_user)