from django.contrib import admin

# Register your models here.
from .models import (
    Service,
    Establishment,
    Professional,
    Address
)

admin.site.register(Service)
admin.site.register(Establishment)
