from rest_framework import viewsets, filters, permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from application.serializers import AddressSerializer, ApplicantSerializer
from application.models import Address, Applicant
from application.filters import ApplicantFilter


# Create your views here.
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = ApplicantFilter
    search_fields = ('first_name','income')
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
