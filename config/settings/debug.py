from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

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
