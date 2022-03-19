from .base import *
from os import getenv
import django_heroku
import cloudinary
import cloudinary_storage


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

django_heroku.settings(locals())

MEDIA_ROOT = BASE_DIR / 'uploads'

MEDIA_URL = '/uploaded-images/'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME'),
    'API_KEY': os.getenv('API_KEY'),
    'API_SECRET': os.getenv('API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'