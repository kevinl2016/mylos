import django_filters
from django.db.models import Q
from application.models import Applicant, Address

class ApplicantFilter(django_filters.rest_framework.FilterSet):
    address = django_filters.CharFilter(
        name = 'address__address_line__contains',
        method = 'filter_address'
    )
    def filter_address(self,queryset,name,value):
        return queryset.filter(Q(**{name: value}))

    class Meta:
        model = Applicant
        fields = ['address']
