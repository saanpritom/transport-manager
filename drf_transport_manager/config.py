"""This config file holds the variable data needed for the package to run. Usually this values check for
   the settings.py file for the config values if not found then it will set the most popular values for that
   kind of property. If you need to change anything then change it carefully"""

from django.conf import settings


default_media_directory = 'media/'


# Return the Media directory of the project
def get_media_directory(file_location):
    if hasattr(settings, 'MEDIA_ROOT'):
        # If the forward slash / is present on the first character then removing it.
        if settings.MEDIA_URL[0] == '/':
            return str(settings.MEDIA_URL[1:]) + str(file_location)
        else:
            return str(settings.MEDIA_URL) + str(file_location)
    else:
        return str(default_media_directory) + str(file_location)
