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
