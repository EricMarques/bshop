from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from datetime import datetime

from .models import (
    Service,
    Address,
    Professional,
    Establishment,
)


class ServiceModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = []


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = []


class ProfessionalModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    address = AddressModelSerializer()

    class Meta:
        model = Professional
        exclude = []


class EstablishmentModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    address = AddressModelSerializer()

    class Meta:
        model = Establishment
        exclude = []
