from rest_framework import viewsets
from app.models import (
    Service,
    Professional,
    Establishment,
)

from ..serializers import (
    ServiceModelSerializer,
    ProfessionalModelSerializer,
    EstablishmentModelSerializer,
)


class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceModelSerializer
    queryset = Service.objects.all()


class ProfessionalsViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionalModelSerializer
    queryset = Professional.objects.all()


class EstablishmentsViewSet(viewsets.ModelViewSet):
    serializer_class = EstablishmentModelSerializer
    queryset = Establishment.objects.all()
