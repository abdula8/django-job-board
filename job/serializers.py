# get data from models ------ convert it to -----> json
# like forms.py
from rest_framework import routers, serializers, viewsets
from .models import Job


# Serializers define the API representation.
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
