from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', u'https://project-np.herokuapp.com/']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'db-project-np.cuhffvh7u64m.ap-northeast-2.rds.amazonaws.com',
        'NAME': 'project_NP',
        'USER': 'NPadmin',
        'PASSWORD': get_secret("DATABASE"), 
        'PORT': '5432',
    }
}




STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AWS_ACCESS_KEY_ID = get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=get_secret("AWS_SECRET_ACCESS_KEY")
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'projectnp-bucket'
AWS_S3_CUSTOM_DOMAIN = f's3.{AWS_REGION}.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}'

AWS_S3_FILE_OVERWRITE = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = ''

DATA_UPLOAD_MAX_MEMORY_SIZE = 1024000000 # value in bytes 1GB here
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024000000

DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'
STATICFILES_STORAGE = 'config.storages.S3StaticStorage'