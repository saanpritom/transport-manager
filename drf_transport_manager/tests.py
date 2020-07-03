from django.test import TestCase
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth import get_user_model
from .configs import get_media_directory
from .models import TransportAgencyModel


# Create your tests here.
class ConfigModulesTestCase(TestCase):

    # Testing the get_media_directory function output
    def test_get_media_directory(self):
        self.assertRaises(TypeError, get_media_directory)
        self.assertRaises(ValidationError, get_media_directory, '')
        self.assertRaises(ValidationError, get_media_directory, '/media/')
        if hasattr(settings, 'MEDIA_ROOT'):
            self.assertEqual(get_media_directory('images/hello'), str(settings.MEDIA_URL[1:]) + 'images/hello')
        self.assertEqual(get_media_directory('images/hello'), 'media/images/hello')


class ModelInitialDataTestCase(TestCase):

    def setUp(self):
        get_user_model().objects.create_user('test_admin', 'test_admin@example.com')
        TransportAgencyModel.objects.create()

    # Testing models dependent initial data
    def test_transport_agency_model_initial_data(self):
        self.assertEqual(TransportAgencyModel.objects.get(id=1).agency_name, 'N/A')
