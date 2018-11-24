from django.db import models
# from tenant_schemas.models import TenantMixin
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created_on = models.DateField(auto_now_add=True)

    # auto_create_schema = True


class Domain(DomainMixin):
    pass