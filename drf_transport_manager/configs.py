"""This config file holds the variable data needed for the package to run. Usually this values check for
   the settings.py file for the config values if not found then it will set the most popular values for that
   kind of property. If you need to change anything then change it carefully"""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import ValidationError


default_media_directory = 'media/'


# Return the Media directory of the project
def get_media_directory(file_location):
    if file_location != '':
        if file_location[0] != '/':
            if hasattr(settings, 'MEDIA_ROOT'):
                # If the forward slash / is present on the first character then removing it.
                if settings.MEDIA_URL[0] == '/':
                    return str(settings.MEDIA_URL[1:]) + str(file_location)
                else:
                    return str(settings.MEDIA_URL) + str(file_location)
            else:
                return str(default_media_directory) + str(file_location)
        else:
            raise ValidationError('File location cannot be an absolute path. Remove / from first character')
    else:
        raise ValidationError('File location argument cannot be empty')


# Return the default User ID of the system
def get_default_user_id():
    # Check if there is superuser, If True then return the ID of the Superuser
    if get_user_model().objects.filter(Q(is_superuser=True) and Q(is_active=True)).exists():
        return get_user_model().objects.filter(Q(is_superuser=True) and Q(is_active=True)).first().id
    # If superuser not existed then check if staff user exists and send it's id
    elif get_user_model().objects.filter(Q(is_staff=True) and Q(is_active=True)).exists():
        return get_user_model().objects.filter(Q(is_staff=True) and Q(is_active=True)).first().id
    # If no staff user exists then simply return the first user id
    elif get_user_model().objects.filter(is_active=True).exists():
        return get_user_model().objects.filter(is_active=True).first().id
    # If nothing existed then just return 1
    else:
        return 1
