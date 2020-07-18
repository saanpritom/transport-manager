from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import TransportAgencyModel


class TransportAgencyModelTestCase(TestCase):

    def setUp(self):
        get_user_model().objects.create_user('test_admin', 'test_admin@example.com')
        TransportAgencyModel.objects.create()

    # Testing models dependent initial data
    def test_transport_agency_model_initial_data(self):
        self.assertEqual(TransportAgencyModel.objects.get(id=1).agency_name, 'N/A')
