"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.

#BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if os.path.isfile(os.path.join(BASE_DIR, '.secrets.json'))==True:
    ##LOCAL
    secret_file = os.path.join(BASE_DIR, '.secrets.json')

    with open(secret_file) as f:
        secrets = json.loads(f.read())

    def get_secret(setting, secrets=secrets):
        try:
            return secrets[setting]
        except KeyError:
            error_msg = "Set the {} env var".format(setting)
            raise ImproperlyConfigured(error_msg)

    SECRET_KEY              = get_secret("SECRET_KEY")
    DATABASE_PASSWORD       = get_secret("DATABASE")
    AWS_ACCESS_KEY_ID       = get_secret("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY   = get_secret("AWS_SECRET_ACCESS_KEY")
    KAKAO_MAP_API_KEY       = get_secret("KAKAO_MAP_API_KEY")
    
else:
    ##DEPLOY
    SECRET_KEY              = os.environ.get("SECRET_KEY")
    DATABASE_PASSWORD       = os.environ.get("DATABASE")
    AWS_ACCESS_KEY_ID       = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY   = os.environ.get("AWS_SECRET_ACCESS_KEY")
    KAKAO_MAP_API_KEY       = os.environ.get("KAKAO_MAP_API_KEY")

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',

#APP
    'myside',
    'community',
    'accounts',
    'mycvs',
        
#Library
    'mptt',                 #카테고리
    'taggit',               #태그
    'ckeditor',             #커뮤니티 글 쓰기 폼
    'ckeditor_uploader',

#all-auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 

#for DRF
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',

#for React
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
            ['Image','Table','HorizontalRule','SpecialChar'],
        ],
        'height': 600,
        'width': 900,
    }
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',               
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#인증 관련
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',

    ]
}

#커스텀 로그인, user 정보 사용
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'accounts.serializers.LoginSerializer',
#    'TOKEN_SERIALIZER': 'accounts.serializers.TokenSerializer',
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
}

#커스텀 serializer 사용
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.RegisterSerializer',
}

#커스텀 adapter
ACCOUNT_ADAPTER = 'accounts.adapter.CustomAccountAdapter'


#커스텀 User Model
AUTH_USER_MODEL = 'accounts.User'


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

#이메일 인증
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'   #이메일 주소가 확인 되기 전까지 로그인 차단                 
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/account/registration/confirm_email/?verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/account/registration/confirm_email/?verification=1'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

'''
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587 
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = 'gmail_username' 
EMAIL_HOST_PASSWORD = 'password from https://security.google.com/settings/security/apppasswords' 
'''

OLD_PASSWORD_FIELD_ENABLED = True
########################################################
SITE_ID = 1

#REST_USE_JWT = True

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MPTT_ADMIN_LEVEL_INDENT = 20


CKEDITOR_UPLOAD_PATH = "communities/"
