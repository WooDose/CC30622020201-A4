from parents_app.models import Parent
from rest_framework import serializers

class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = (
            'id',
            'first_name'
        )