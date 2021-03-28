from rest_framework import serializers

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


class ProfessionalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        exclude = ['updated_at']


class ProfessionalCreateModelSerializer(serializers.ModelSerializer):
    address = AddressModelSerializer(read_only=True)

    class Meta:
        model = Professional
        exclude = ['updated_at']


class EstablishmentModelSerializer(serializers.ModelSerializer):
    address = AddressModelSerializer()

    class Meta:
        model = Establishment
        exclude = ['updated_at']
