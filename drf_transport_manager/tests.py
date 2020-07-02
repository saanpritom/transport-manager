from django.test import TestCase
from django.core.exceptions import ValidationError
from django.conf import settings
from .configs import get_media_directory


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
