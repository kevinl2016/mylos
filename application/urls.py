from rest_framework import routers
from application.views import AddressViewSet, ApplicantViewSet

router = routers.SimpleRouter()
router.register('address',AddressViewSet)
router.register('applicants', ApplicantViewSet)
