from django.shortcuts import render
from ..models import (
    Professional,
    Service,
    Establishment
)

from django.views.generic import TemplateView

from ..services import (
    count_professionals,
    count_services,
    count_establishment,
)


def show_index(request):
    return render(request, 'base.html')


def show_dashboard(request):

    context = {
        'count_professionals': count_professionals(),
        'count_services': count_services(),
        'count_establishments': count_establishment(),
    }

    return render(request, 'pages/dashboard/dashboard.html', context=context)
