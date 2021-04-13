import os
import requests


# SERVICES
def list_services():
    url = 'http://localhost:8000/api/service'
    service = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    services = service.json()
    service_list = []

    for i in range(len(services['results'])):
        service_list.append(services['results'][i])

    return service_list


def count_services():
    url = 'http://localhost:8000/api/service'
    service = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    services = service.json()

    return services['count']


# ESTABLISHMENTS
def list_establishments():
    url = 'http://localhost:8000/api/establishment'
    establishment = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    establishments = establishment.json()
    establishment_list = []

    for i in range(len(establishments['results'])):
        establishment_list.append(establishments['results'][i])

    return establishment_list


def count_establishment():
    url = 'http://localhost:8000/api/establishment'
    establishment = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    establishments = establishment.json()

    return establishments['count']


# PROFESSIONALS
def list_professionals():
    url = 'http://localhost:8000/api/professional'
    professional = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    professionals = professional.json()
    professional_list = []

    for i in range(len(professionals['results'])):
        professional_list.append(professionals['results'][i])

    return professional_list


def count_professionals():
    url = 'http://localhost:8000/api/professional'
    professional = requests.get(url, headers={'Authorization': 'Bearer %s' % os.getenv('DO_ACCESS_TOKEN')})
    professionals = professional.json()

    return professionals['count']
