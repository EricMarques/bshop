from django.shortcuts import render
from ..models import (
    Professional,
    Service,
    Establishment
)

from django.views.generic import TemplateView


def show_index(request):
    return render(request, 'base.html')


def show_dashboard(request):
    count_professionals = Professional.objects.count()
    count_services = Service.objects.count()
    count_establishments = Establishment.objects.count()

    context = {
        'count_professionals': count_professionals,
        'count_services': count_services,
        'count_establishments': count_establishments,
    }

    print("Total de profissionais: {}".format(count_professionals))

    return render(request, 'pages/dashboard/dashboard.html', context=context)


class CountProfessionals(TemplateView):
    template_name = 'pages/dashboard/dashboard.html'

    def count_professionals(self):
        count_professionals = Professional.objects.count()

        return count_professionals
