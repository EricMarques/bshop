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
        #  fields = '__all__'
        '''
        fields=[
            'id',
            'name',
            'description',
            'price',
            'professional',
            'status',
            'created_at',
            'updated_at',
        ]
        '''


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['updated_at']
        #  fields = '__all__'
        '''
        fields=[
            'id',
            'street',
            'number',
            'complement',
            'neighborhood',
            'city',
            'state',
            'country',
            'created_at',
            'updated_at',
        ]
        '''


class ProfessionalModelSerializer(serializers.ModelSerializer):
    address = AddressModelSerializer()

    class Meta:
        model = Professional
        exclude = ['updated_at']
        #  fields = '__all__'
        '''
        fields=[
            'id',
            'first_name',
            'second_name',
            'birth_date',
            'gender',
            'address',
            'status',
            'created_at',
            'updated_at',
        ]
        '''


class EstablishmentModelSerializer(serializers.ModelSerializer):
    address = AddressModelSerializer()

    class Meta:
        model = Establishment
        exclude = ['updated_at']
        #  fields = '__all__'
        '''
        fields=[
            'id',
            'name',
            'company_name',
            'registered_number',
            'municipal_registration',
            'address',
            'status',
            'created_at',
            'updated_at',
        ]
        '''
