"""
Django settings for earth project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
# 배포용
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# 환경변수 세팅
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('DJANGO_SECRET')

AWS_ACCESS_KEY_ID =  get_env_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =  get_env_variable('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME =  get_env_variable('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME =  get_env_variable('AWS_S3_REGION_NAME')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = None

# S3 버킷을 기본 스토리지로 설정
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


DEBUG = True

# 배포
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".cloudtype.app"]
CSRF_TRUSTED_ORIGINS = ['https://*.cloudtype.app']

# 모든 외부 도메인 요청 허용
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# 일부 도메인 요청 허용
# CORS_ORIGIN_ALLOW_WHITELIST = (

# )


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'join.apps.JoinConfig',
    # 'users.apps.UsersConfig',

    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'drf_yasg',
    'storages',
    # 'rest_framework_simplejwt',

    # 앱
    'users',
    'join',
    'market',
    'us',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'earth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'earth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DBNAME = get_env_variable('DBNAME')
DBUSER = get_env_variable('DBUSER')
DBPASSWORD = get_env_variable('DBPASSWORD')
DBHOST = get_env_variable('DBHOST')
DBPORT = get_env_variable('DBPORT')

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.mysql',
        'NAME': DBNAME,
        'USER': DBUSER,
        'PASSWORD': DBPASSWORD, 
        'HOST': DBHOST, 
        'PORT': DBPORT,
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50),  # 액세스 토큰의 만료 시간
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # 리프레시 토큰의 만료 시간
}