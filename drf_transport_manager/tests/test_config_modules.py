from django.test import TestCase
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth import get_user_model
from ..configs import (get_media_directory, get_default_user_id)


# Create your tests here.
class ConfigModulesTestCase(TestCase):

    def setUp(self):
        get_user_model().objects.create_user('test_admin', 'test_admin@example.com')
        get_user_model().objects.create_user('test_admin_two', 'test_admin_two@example.com')

    # Testing the get_media_directory function output
    def test_get_media_directory(self):
        self.assertRaises(TypeError, get_media_directory)
        self.assertRaises(ValidationError, get_media_directory, '')
        self.assertRaises(ValidationError, get_media_directory, '/media/')
        if hasattr(settings, 'MEDIA_ROOT'):
            self.assertEqual(get_media_directory('images/hello'), str(settings.MEDIA_URL[1:]) + 'images/hello')
        self.assertEqual(get_media_directory('images/hello'), 'media/images/hello')

    # Testing the get_default_user_id funtion output
    def test_get_default_user_id(self):
        self.assertRaises(TypeError, get_default_user_id, 1)
        self.assertEqual(get_default_user_id(), 1)
