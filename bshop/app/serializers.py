from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import (
    Service,
    Address,
    Professional,
    Establishment,
)


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['updated_at']


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['updated_at']


class ProfessionalModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    # service = ServiceModelSerializer(many=True)
    address = AddressModelSerializer()

    class Meta:
        model = Professional
        exclude = ['updated_at']


class EstablishmentModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    address = AddressModelSerializer()

    class Meta:
        model = Establishment
        exclude = ['updated_at']
