from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','3.34.97.145']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'database-np.cuhffvh7u64m.ap-northeast-2.rds.amazonaws.com',
        'NAME': 'DatabaseNP',
        'USER': 'myside',
        'PASSWORD': DATABASE_PASSWORD, 
        'PORT': '5432',
    }
}





AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'bucket-np'
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

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

