from rest_framework import serializers
from babies_app.models import Baby
from parents_app.serializers import ParentSerializer


class BabySerializer(serializers.ModelSerializer):

    class Meta:
        model = Baby
        fields = (
            'id',
            'first_name',
            'last_name',
            'parent_id'
        )