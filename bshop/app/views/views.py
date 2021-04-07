from django.shortcuts import (
    render
)

from django.views.generic import TemplateView

from rest_framework import viewsets

from app.models import (
    Service,
    Professional,
    Establishment,
)

from ..serializers import (
    ServiceModelSerializer,
    ProfessionalModelSerializer,
    ProfessionalCreateModelSerializer,
    EstablishmentModelSerializer,
)

import requests
from ..services import (
    list_services,
    list_establishments,
    list_professionals,
)


class ServicesViewSet(viewsets.ModelViewSet):
    """
        List/Add SERVICES
    """
    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer


class ProfessionalsViewSet(viewsets.ModelViewSet):
    """
        List/Add PROFESSIONALS
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalModelSerializer

    def get_serializer_class(self):
        actions = [
            'create',
            'update',
            'partial_update'
        ]
        if self.action in actions:
            return ProfessionalCreateModelSerializer

        return self.serializer_class


class EstablishmentsViewSet(viewsets.ModelViewSet):
    """
        List/Add ESTABLISHMENTS
    """
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentModelSerializer


class GetServices(TemplateView):
    template_name = 'pages/service/list_services.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'services': list_services(),
            # 'services_empty': []
        }
        print(context)
        return context


class GetEstablishments(TemplateView):
    template_name = 'pages/service/list_establishments.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'establishments': list_establishments(),
            # 'establishments_empty': []
        }
        print(context)
        return context


class GetProfessionals(TemplateView):
    template_name = 'pages/professional/list_professionals.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'professionals': list_professionals(),
            # 'establishments_empty': []
        }
        print(context)
        return context


def check_postal_code(_postal_code_input):
    if 'erro' not in _postal_code_input:
        postal_code = requests.get('https://viacep.com.br/ws/{}/json/'.format(_postal_code_input))
        address = postal_code.json()
        street = address['street']
        neigborhood = address['neigborhood']
        city = address['city']
        state = address['state']
        country = address['country']

        return
    else:
        return 'CEP inválido!'
