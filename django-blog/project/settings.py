"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG =  os.environ.get('DEBUG') == 'True'
DEBUG = True


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','').split(',')
# ALLOWED_HOSTS = ['192.168.0.108']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Main Project as an app
    'project',

    # Other Local Apps
    'blog.apps.BlogConfig', 
    'blog_api',

    # Third parties
    # 'sass_processor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    # 'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',
    #cors orign
    'corsheaders',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),        
        #'PASSWORD': 'rhprince', #os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
        'TEST':{
            'NAME': 'budget_test'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# This is for app level static files dirs
STATIC_URL = '/static/'

# This as a combined static files dirs. 
# It will be colect all static files after collectstatic command
# On production, server will use this 
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# django-sass-processor settings

# SASS_PROCESSOR_ROOT = STATIC_ROOT
# SASS_PROCESSOR_ENABLED = os.environ.get('DEBUG', False) == 'True'
# # SASS_PROCESSOR_ENABLED = False

# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'sass_processor.finders.CssFinder',
# ]




LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 2 
# because default site example.com is 1.
# Created a new site. it's id should be 2


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else: 
#   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# for gmail or google apps
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER =  email
# EMAIL_HOST_PASSWORD = password
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False



## CACHING  with Redis
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "blog"
#     }
# }

# cache time to live is 15 minutes
# CACHE_TTL = 60 * 15 

# rest framework settings

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 10
# }


#CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = tuple(
    os.environ.get(
        'CORS_ORIGIN_WHITELIST',
        'http://localhost:3000',
    ).split()
)